from agents import Agent

bank_agent = Agent(
    name="Bank Agent",
    instructions="You help customers check balances.",
    tools=[],  # No tools added yet
    model="gpt-4o",  # Optional
    parallel_tool_calls=True
)
