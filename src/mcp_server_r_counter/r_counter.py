from mcp.server.fastmcp import FastMCP

mcp = FastMCP("r_counter")

@mcp.tool()
async def count(query: str) -> str:
    """Count number of R's or r's in the input query"""
    return str(query.lower().count("r"))

def main():
    mcp.run()