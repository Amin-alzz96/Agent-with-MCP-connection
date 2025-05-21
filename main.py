import json
from langchain_mcp_adapters.client import MultiServerMCPClient
from llm_config import llm
from langchain.agents import initialize_agent, AgentType
import asyncio

# Load MCP server config
def load_mcp_config(path="conf.json"):
    with open(path, "r") as f:
        return json.load(f)["mcpServers"]

async def setup_mcp_tools():
    mcp_servers = load_mcp_config()
    # Convert config to the format expected by MultiServerMCPClient
    for server in mcp_servers.values():
        if "transport" not in server:
            server["transport"] = "stdio"
    client = MultiServerMCPClient(mcp_servers)
    tools = await client.get_tools()
    return tools

async def main():
    llm_instance = llm()
    tools = await setup_mcp_tools()
    agent = initialize_agent(
        tools=tools,
        llm=llm_instance,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
    )
    result = await agent.arun(
        "Scrape the text of all <h1> elements from https://en.wikipedia.org/wiki/Artificial_intelligence using the selector 'h1' and return the results."
    )
    print("Agent result:", result)

if __name__ == "__main__":
    asyncio.run(main())

