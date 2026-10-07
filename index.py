"""Vercel ASGI entry point for the stateless Streamable HTTP MCP server."""

from contextlib import asynccontextmanager
from typing import AsyncIterator

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Mount

from dcom_mcp.server import mcp


@mcp.custom_route("/healthz", methods=["GET"], include_in_schema=False)
async def healthz(_: Request) -> PlainTextResponse:
    return PlainTextResponse("ok")


mcp_app = mcp.streamable_http_app()


@asynccontextmanager
async def lifespan(_: Starlette) -> AsyncIterator[None]:
    # FastMCP 1.30's returned app does not own the session manager lifespan;
    # Vercel's top-level ASGI app must start it explicitly.
    async with mcp.session_manager.run():
        yield


app = Starlette(routes=[Mount("/", app=mcp_app)], lifespan=lifespan)
