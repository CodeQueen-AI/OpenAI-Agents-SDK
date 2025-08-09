from agents import Agent, Runner, function_tool
from config import config

@function_tool
def add_numbers(a: int, b: int) -> int:
    """Returns the sum of two numbers"""
    return a + b

agent = Agent(
    name='Math Agent',
    instructions='You are a calculator. Use tools to answer math questions.',
    tools=[add_numbers]  # 👈 Tool agent ke sath attach
)

# 🚀 3. Agent ko run karte hain tool call ke sath
result = Runner.run_sync(
    agent,
    "What is the sum of 5 and 7?",
    run_config=config
)

# 📤 4. Output print
print(result.final_output)
