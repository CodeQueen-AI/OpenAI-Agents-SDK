from agents import Agent, Runner , function_tool
from config import config
import asyncio

# ✅ Reusable Tool
@function_tool
def greet(name: str) -> str:
    """User ka naam le kar greeting return karta hai."""
    return f"Hello, {name}! Welcome 😊"

# ✅ Agent 1: GreetBot
agent1 = Agent(
    name="GreetBot",
    instructions="Greet the user by name.",
    tools=[greet]
)

# ✅ Agent 2: WelcomeBot
agent2 = Agent(
    name="WelcomeBot",
    instructions="Start responses with greetings.",
    tools=[greet]
)

# ✅ Runner
async def main():
    result1 = await Runner.run(
        starting_agent=agent1,
        input="Greet Sumbal",
        run_config=config
    )

    result2 = await Runner.run(
        starting_agent=agent2,
        input="Say hello to Zara",
        run_config=config
    )

    print("Agent 1 Output:", result1.final_output)
    print("Agent 2 Output:", result2.final_output)

asyncio.run(main())
