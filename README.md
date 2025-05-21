# LangChain Agent with MCP Web Scraper Tool

This project demonstrates a proof-of-concept (POC) for connecting a LangChain (or LangGraph) agent to a custom Model Context Protocol (MCP) tool. The MCP tool is a web scraper that extracts data from any website using a CSS selector. The agent can invoke this tool as part of its reasoning process.

## Features
- **MCP Server**: Exposes a web scraping tool via MCP protocol.
- **LangChain Agent**: Connects to the MCP tool and an LLM (OpenAI GPT-4o-mini by default).
- **Async Integration**: Uses async agent and tool invocation for compatibility.
- **Configurable**: Server configuration via `conf.json`.

---

## Quick Start Guide

### 1. Prerequisites
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) for dependency management (or use pip if preferred)
- OpenAI API key (for LLM)

### 2. Clone the Repository
```sh
git clone <your-repo-url>
cd 08_MCP_Agent
```

### 3. Install Dependencies
```sh
uv pip install -r requirements.txt
# OR, if using pyproject.toml:
uv sync
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your-openai-api-key
```


### 5. Run the Agent
In another terminal:
```sh
python main.py
```

You should see the agent invoke the web scraper tool and print the results.

---

## Project Structure
- `main.py` — Entry point; runs the async agent and connects to the MCP tool.
- `mcp_server.py` — Defines and serves the web scraping MCP tool.
- `llm_config.py` — LLM (OpenAI) configuration.
- `conf.json` — MCP server configuration.
- `pyproject.toml` — Project dependencies.
- `README.md` — This file.

---

## How It Works
1. **MCP Server**: `mcp_server.py` registers a `scrape_website` tool that takes a URL and CSS selector, returning the text and attributes of matching elements.
this app is designed to run locally so please make necessary changes in `conf.json` file. 
2. **Agent**: `main.py` loads the MCP tool using `langchain_mcp_adapters`, connects it to the LLM, and runs an async agent loop.
3. **Example**: The agent is prompted to scrape all `<h1>` elements from a sample website.

---

## Customization
- To add more MCP tools, define them in `mcp_server.py` and update `conf.json`.
- To use a different LLM, modify `llm_config.py`.


## License
MIT
