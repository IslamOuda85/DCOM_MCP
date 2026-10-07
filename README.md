# DCOM_MCP

A read-only MCP server for a specific Data Communications course. It retrieves textbook sections, chapter data cards, original figures, and practice questions linked to the section being studied.

**Current release:** Chapters 1, 2, and 4–7 are reviewed and available. Chapters 3, 8–10, 12, and 13 are being repaired and are not served as verified content. Chapter 11 is outside this course's configured scope. See [release status](course/release.json) and [review records](course/reviews).

## Course grounding

The primary source is *Data Communications and Networking*, Behrouz A. Forouzan, 5th edition (2013). Slides are supporting material. Historical descriptions remain tied to that edition. Extracted course content and textbook figures retain their original source attribution; this project does not assign a new license to the textbook material.

Each released chapter has `content.md`, `questions.md`, `data_card.md`, and `assets/manifest.json`. Source figures have captions, visible text, spatial descriptions, section IDs, usage guidance, and image hashes. Reused figures have one asset definition and multiple `ASSET_REF` references.

## Run locally

Use Python 3.11 or newer. From a clone of this repository:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -e ".[dev]"
.venv\Scripts\python.exe tools/validate_release.py
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe -m dcom_mcp.server
```

The final command starts stdio transport and waits for an MCP client. On Linux/macOS use `.venv/bin/python` instead. `COURSE_ROOT` defaults to this checkout when using an editable installation; set it explicitly when installing elsewhere.

### Claude Desktop and other stdio clients

Configure the client with an absolute interpreter path and course checkout path:

```json
{
  "mcpServers": {
    "DCOM_MCP": {
      "command": "C:/path/to/DCOM_MCP/.venv/Scripts/python.exe",
      "args": ["-m", "dcom_mcp.server"],
      "env": {"COURSE_ROOT": "C:/path/to/DCOM_MCP"}
    }
  }
}
```

Install [the teaching instructions](teaching/system_prompt.md) in the host's tutor instructions if that client does not apply MCP server instructions automatically. The MCP provides context; the host model produces explanations.

### HTTP and ChatGPT

```powershell
.venv\Scripts\python.exe -m dcom_mcp.server --http
```

The default local endpoint is `http://127.0.0.1:8000/mcp`. For a remote deployment, terminate TLS at your host, set `MCP_HOST=0.0.0.0`, `MCP_ALLOWED_HOSTS` to the deployment hostname (and port if needed), and `MCP_ALLOWED_ORIGINS` to the exact allowed web origin. DNS rebinding protection remains enabled. A Dockerfile is included; publishing this GitHub repository does not deploy a running endpoint.

ChatGPT supports custom MCP servers through an HTTPS server URL or a Secure MCP Tunnel. In ChatGPT Plugins, add a custom MCP server, configure its connection and authentication, then install the resulting plugin. Account/workspace availability is controlled by ChatGPT. See [OpenAI's connection guide](https://developers.openai.com/api/docs/guides/custom-mcp-server). No hosted endpoint has been provisioned for this repository yet.

This server exposes public course context and no write tools. It has no built-in user accounts or OAuth. If a host requires authentication, configure it at a compatible gateway; never label an unauthenticated deployment as protected.

## Retrieval workflow

1. `get_course_metadata` and `list_chapters`: check available material.
2. `search_course`: locate relevant source sections.
3. `get_section` / `get_teaching_context`: retrieve complete context with source citations.
4. `get_asset`: return the actual image with its description as MCP content.
5. `list_questions(section_id=...)` and `get_question`: practice the section just studied.

`search` and `fetch` aliases support clients expecting those tool names. `course://metadata`, `course://teaching`, and the `teach_section` prompt are also provided. Clients must support MCP; an arbitrary chatbot without tool integration cannot use this server directly.

## Index and release integrity

The [semantic routing index](course/semantic_index.json) records source hierarchy, stable IDs, terms, linked assets, and practice questions. Ranking uses BM25 plus curated acronym expansion. It does not use embeddings or require a model API key.

Only `ready` entries in `course/release.json` are loaded. Every released file, including each image, is fingerprinted. A mismatch or unresolved data-card issue excludes the chapter. A file changed after startup causes retrieval to fail until a reviewed release is rebuilt and the server restarted.

To update a checkout, pull the intended Git commit, install its dependencies, run validation, and restart the MCP. Data is read from the local versioned checkout, not downloaded from GitHub during each tool call. This keeps a lesson consistent with a specific release.

## Validation

```powershell
python tools/validate_release.py
python tools/build_index.py
python -m pytest -q
```

Validation checks source-review receipts, question/section/figure links, one canonical asset definition, metadata counts, image hashes and dimensions, encoding, and release fingerprints. Automated checks do not prove complete textbook fidelity by themselves; source review is recorded separately before a chapter is promoted.

The Chapter 1 source notes document the printed `DLS` typo in Q1-15 and the protocol-layering question Q1-16 that belongs to Chapter 2 section 2.1.2. Q1-16 remains source-faithful and explicitly reports when its dependency is not yet released.
