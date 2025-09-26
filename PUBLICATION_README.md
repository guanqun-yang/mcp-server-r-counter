# MCP Server Publication Guide

This document outlines the complete process for publishing an MCP server to both PyPI and the Anthropic MCP registry.

## Prerequisites

- PyPI account created
- GitHub account (for namespace authentication)
- MCP server code ready

## Step 1: Prepare Package Configuration

### Update pyproject.toml
Ensure your `pyproject.toml` has the correct structure:

```toml
[project]
name = "mcp-server-r-counter"
version = "0.0.3"
description = "A MCP Server Counting Number of r's for a Given Query"
readme = "README.md"
dependencies = [
    "mcp>=1.4.1",
]

[project.scripts]
mcp-server-r-counter = "mcp_server_r_counter:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

Key points:
- Include `readme = "README.md"` to display README on PyPI
- Define entry point in `[project.scripts]`
- Specify build system

## Step 2: Add MCP Registry Validation to README

Add the MCP validation line to your `README.md`:

```markdown
# MCP Server R Counter

A Model Context Protocol (MCP) server that counts the number of 'r' characters in a given query.

mcp-name: io.github.guanqun-yang/mcp-server-r-counter

## Installation
...
```

**Important**: The `mcp-name: io.github.yourname/mcp-server-name` line must appear in the README that gets displayed on PyPI.

## Step 3: Build and Publish to PyPI

### Install Publishing Tools
```bash
pip install build twine
```

### Build the Package
```bash
python -m build
```

This creates:
- `dist/mcp_server_r_counter-0.0.3.tar.gz` (source distribution)
- `dist/mcp_server_r_counter-0.0.3-py2.py3-none-any.whl` (wheel)

### Upload to PyPI
```bash
twine upload dist/*
```

Enter your PyPI credentials when prompted.

## Step 4: Publish to MCP Registry

### Install MCP Publisher CLI
```bash
brew install mcp-publisher
```

### Create server.json Configuration
Create a `server.json` file with this structure:

```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-09-16/server.schema.json",
  "name": "io.github.guanqun-yang/mcp-server-r-counter",
  "description": "A MCP Server Counting Number of r's for a Given Query",
  "status": "active",
  "repository": {
    "url": "https://github.com/guanqun-yang/mcp-server-r-counter",
    "source": "github"
  },
  "version": "0.0.3",
  "packages": [
    {
      "registryType": "pypi",
      "registryBaseUrl": "https://pypi.org",
      "identifier": "mcp-server-r-counter",
      "version": "0.0.3",
      "transport": {
        "type": "stdio"
      }
    }
  ]
}
```

### Authenticate with GitHub
```bash
mcp-publisher login github
```

Follow the device flow authentication process.

### Publish to MCP Registry
```bash
mcp-publisher publish
```

## Common Issues and Solutions

### PyPI Package Ownership Validation Failed
**Error**: `PyPI package 'mcp-server-r-counter' ownership validation failed. The server name 'io.github.yourname/mcp-server-name' must appear as 'mcp-name: io.github.yourname/mcp-server-name' in the package README`

**Solution**:
1. Add the `mcp-name:` line to your README.md
2. Ensure `readme = "README.md"` is in pyproject.toml
3. Increment version number
4. Rebuild and re-upload to PyPI
5. Retry MCP registry publication

### Version Mismatches
Ensure versions match across:
- `pyproject.toml` version field
- `server.json` version field
- `server.json` packages.version field

## Complete Command Sequence

```bash
# 1. Build package
python -m build

# 2. Upload to PyPI
twine upload dist/*

# 3. Authenticate with MCP registry
mcp-publisher login github

# 4. Publish to MCP registry
mcp-publisher publish
```

## Success Indicators

- PyPI upload: "Upload successful" message
- MCP registry: "✓ Successfully published" with server ID
- Server ID format: `d25dab7d-1a05-4679-b314-a2911998f316`

## Post-Publication

Users can install your server via:
```bash
pip install mcp-server-r-counter
```

The server becomes discoverable through MCP-compatible clients that browse the registry.