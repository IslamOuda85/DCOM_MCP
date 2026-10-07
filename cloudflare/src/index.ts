import { Container, getContainer } from "@cloudflare/containers";

interface Env {
  DCOM_MCP: DurableObjectNamespace<DcomMcpContainer>;
}

/** Runs the existing Python MCP image inside a Cloudflare Container. */
export class DcomMcpContainer extends Container<Env> {
  defaultPort = 8000;
  sleepAfter = "10m";
  pingEndpoint = "/";
  enableInternet = false;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/healthz") {
      return new Response("ok", { headers: { "content-type": "text/plain" } });
    }

    // The Python server's transport-security layer is kept enabled. The Worker
    // terminates the public hostname and forwards a local, trusted Host value.
    const headers = new Headers(request.headers);
    headers.set("Host", "127.0.0.1:8000");
    headers.delete("Origin");
    const forwarded = new Request(request, { headers });
    return getContainer(env.DCOM_MCP, "singleton").fetch(forwarded);
  },
};
