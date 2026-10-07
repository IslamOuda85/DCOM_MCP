# DCOM_MCP

A read-only MCP server for a specific Data Communications course. It retrieves textbook sections, chapter data cards, original figures, and practice questions linked to the section being studied.

**Current release:** All 12 configured course chapters—1–10, 12, and 13—are source reviewed and available. The release contains 687 indexed sections, 291 described assets, and 382 section-linked practice questions. Chapter 11 is outside this course's configured scope. See [release status](course/release.json) and [review records](course/reviews).

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

ChatGPT supports custom MCP servers through an HTTPS server URL or a Secure MCP Tunnel. In ChatGPT Plugins, add a custom MCP server, configure its connection and authentication, then install the resulting plugin. Account/workspace availability is controlled by ChatGPT. See [OpenAI's connection guide](https://developers.openai.com/api/docs/guides/custom-mcp-server).

This server exposes public course context and no write tools. It has no built-in user accounts or OAuth. If a host requires authentication, configure it at a compatible gateway; never label an unauthenticated deployment as protected.

### Vercel deployment

The repository includes a Python ASGI entry point in [index.py](index.py) for Vercel's Python Functions runtime. It serves the stateless Streamable HTTP MCP endpoint at `/mcp` and a readiness endpoint at `/healthz`. The Vercel function bundle explicitly includes the course release, assets, and teaching instructions. Vercel's Python runtime is currently in Beta; the function bundle must remain within Vercel's published size and duration limits.

Deploy this repository as a **new, separate Vercel project**. Do not connect it to the existing website project or assign it the apex domain `owda.io`. After deploying and checking the Vercel-provided URL, add only `mcp.owda.io` to the new project's Domains settings. At Hostinger, create only the DNS record Vercel specifies for that subdomain; leave the apex and existing website records unchanged. The MCP URL will be `https://mcp.owda.io/mcp`.

Vercel supplies the deployment hostname through `VERCEL_URL`; the server allows that exact hostname for previews, along with the production aliases `dcom-mcp.vercel.app` and `mcp.owda.io`. The allowed-host and allowed-origin protections remain enabled. The root `owda.io` website and its Vercel project are not part of this deployment.

### Cloudflare deployment

The repository includes a Cloudflare Workers + Containers wrapper in [wrangler.jsonc](wrangler.jsonc) and [cloudflare/src/index.ts](cloudflare/src/index.ts). It builds the existing Python Docker image and exposes its streamable HTTP MCP endpoint through a Worker. Deploy from the repository root with Docker running:

```powershell
npm install
npx wrangler login
npx wrangler deploy --config wrangler.jsonc
npx wrangler containers list
```

The resulting Worker URL is the MCP server URL with `/mcp` appended. `/healthz` is a simple readiness check. The first container request can take several minutes while Cloudflare provisions the instance. See the [Cloudflare Containers deployment guide](https://developers.cloudflare.com/containers/get-started/) for account and plan prerequisites.

## Retrieval workflow

1. `get_course_metadata` and `list_chapters`: check available material.
2. `search_course`: locate relevant source sections.
3. `get_section` / `get_teaching_context`: retrieve complete context with source citations.
4. `get_asset`: return the actual image with its description as MCP content.
5. `list_questions(section_id=...)` and `get_question`: practice the section just studied.

`search` and `fetch` aliases support clients expecting those tool names. `course://metadata`, `course://teaching`, and the `teach_section` prompt are also provided. Clients must support MCP; an arbitrary chatbot without tool integration cannot use this server directly.

### Images and teaching artifacts in a chat client

The server returns the original figure through `get_asset` as an MCP image block, alongside descriptive metadata. `get_asset_metadata` includes a `repository_url` for opening the source file. The chat client controls whether that image appears inline or can be returned as a downloadable attachment. If the learner asks to see or download a figure, the tutor should deliver the original image inline or as an actual attachment when supported. If neither works, it should give the returned repository URL and describe the figure. A successful tool call alone does not confirm that the learner saw an image or received a file.

The full [tutor instructions](teaching/system_prompt.md) specify when to create a visual artifact: when requested or when an editable or interactive aid helps a retrieved concept, such as tracing encapsulation, stepping through a protocol, or varying formula inputs. The artifact is a cited, labeled teaching aid after the source explanation; it does not replace the original figure or reveal a practice answer early. The MCP provides source material, while Claude, ChatGPT, or another host creates and displays its own artifacts. For consistent behavior, add these tutor instructions to the client's project or custom instructions as well as using the `get_teaching_methodology` tool.

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

The Chapter 1 source notes document the printed `DLS` typo in Q1-15 and the protocol-layering question Q1-16 that belongs to Chapter 2 section 2.1.2. Q1-16 remains source-faithful and links explicitly to that Chapter 2 section.
