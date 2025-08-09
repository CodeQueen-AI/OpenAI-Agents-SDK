from agents import Agent, Runner, function_tool
from config import config
import asyncio

@function_tool
def get_weather() -> str:
    return "Today's weather is sunny ☀️"

@function_tool
def get_news() -> str:
    return "Top news: AI is changing the world 🌍"

@function_tool
def get_currency() -> str:
    return "1 USD = 300 PKR 💱"

agent = Agent(
    name="MultiTaskBot",
    instructions="Give weather, news, and currency info together.",
    tools=[get_weather, get_news, get_currency]
)

async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="Give me all updates",
        run_config=config
    )
    print(result.final_output)

asyncio.run(main())
