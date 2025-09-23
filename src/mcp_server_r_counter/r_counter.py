from mcp.server.fastmcp import FastMCP
import os
import uvicorn

mcp = FastMCP("r_counter")

@mcp.tool()
async def count(query: str) -> str:
    """Count number of R's or r's in the input query"""
    return str(query.lower().count("r"))

def main():
    transport = os.environ.get("MCP_TRANSPORT", "stdio")

    if transport == "sse":
        # For HTTP deployment, run with custom host/port
        host = os.environ.get("HOST", "0.0.0.0")
        port = int(os.environ.get("PORT", 8000))

        # Get the SSE app and run it with proper host binding
        app = mcp.sse_app
        uvicorn.run(app, host=host, port=port)
    else:
        # Use stdio transport for local development
        mcp.run(transport="stdio")

if __name__ == "__main__":
    main()