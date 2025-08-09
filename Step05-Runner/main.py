# Run Sync Method (run.sync)
from agents import Agent, Runner
from config import config

agent = Agent(
    name="Sync Agent",
    instructions="Give simple and short answers"
)

result = Runner.run_sync(
    agent,
    "What is 2 + 2?",
    run_config=config
)

print(result.final_output)


# Run Async method (run)
import asyncio
from agents import Agent, Runner
from config import config

agent = Agent(
    name="Async Agent",
    instructions="Be helpful and accurate"
)

async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="Who is the founder of Pakistan?",
        run_config=config
    )
    print(result.final_output)

# Run the async function
asyncio.run(main())

