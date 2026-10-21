"""
MCP server for yfinance-ai.

Imports yfinance_ai.py as is and registers every public async method of its
Tools class as an MCP tool, with the schema built from its type hints and
docstring. yfinance_ai.py is not modified; OpenWebUI and ClawHub keep using it.

Run: uvx yfinance-ai
"""

import inspect
import logging
import re
import sys
import typing

from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations

import yfinance_ai

logger = logging.getLogger(__name__)

# OpenWebUI injects these at call time; an MCP client cannot send them.
HIDDEN_PARAMS = {"__event_emitter__", "__user__", "__metadata__"}

VERSION = re.search(r"^version:\s*(\S+)", yfinance_ai.__doc__ or "", re.M)
VERSION = VERSION.group(1) if VERSION else ""


def _adapt(method):
    """Wrap a bound tool method so its MCP schema hides the OpenWebUI-only params."""
    sig = inspect.signature(method)
    hints = typing.get_type_hints(method)
    params = [
        p.replace(annotation=hints.get(p.name, p.annotation))
        for p in sig.parameters.values() if p.name not in HIDDEN_PARAMS
    ]

    async def call(**kwargs):
        logger.info("tool %s called with %s", method.__name__, sorted(kwargs))
        try:
            return await method(**kwargs)
        except Exception:
            logger.error("tool %s failed", method.__name__, exc_info=True)
            raise

    call.__name__ = method.__name__
    call.__doc__ = method.__doc__
    call.__signature__ = sig.replace(parameters=params, return_annotation=hints.get("return", sig.return_annotation))
    call.__annotations__ = {p.name: p.annotation for p in params}
    return call


def build_server():
    """Create the MCP server with every tool registered."""
    tools = yfinance_ai.Tools()
    names = sorted(
        n for n, _ in inspect.getmembers(tools, inspect.iscoroutinefunction) if not n.startswith("_")
    )
    server = MCPServer(
        name="yfinance-ai",
        version=VERSION,
        instructions=(
            "Yahoo Finance data: quotes, history, fundamentals, analysts, options, "
            "holders, funds, crypto, forex, commodities, calendars and market-wide screens. "
            "Data comes from Yahoo Finance through yfinance and may be delayed."
        ),
        website_url="https://github.com/lkcair/yfinance-ai",
    )
    for name in names:
        fn = _adapt(getattr(tools, name))
        server.add_tool(
            fn,
            name=name,
            description=inspect.cleandoc(fn.__doc__ or name),
            annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False,
                                        idempotentHint=True, openWorldHint=True),
        )
    logger.info("yfinance-ai MCP %s: %d tools registered", VERSION, len(names))
    return server


def main():
    """Entry point for the `yfinance-ai` console script (stdio transport)."""
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)
    build_server().run("stdio")


if __name__ == "__main__":
    main()
