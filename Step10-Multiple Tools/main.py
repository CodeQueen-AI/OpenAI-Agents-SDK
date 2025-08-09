from agents import Agent, Runner, function_tool
from config import config

# Tool 1: Add two numbers
@function_tool
def add_numbers(a: int, b: int) -> int:
    """Do numbers ka sum return karta hai."""
    return a + b

# Tool 2: Multiply two numbers
@function_tool
def multiply_numbers(a: int, b: int) -> int:
    """Do numbers ka product return karta hai."""
    return a * b

# Tool 3: Convert number to string
@function_tool
def convert_to_string(value: int) -> str:
    """Number ko string mein convert karta hai."""
    return str(value)


agent = Agent(
    name="Calculator Agent",
    instructions="You are a helpful Assistant",
    tools=[add_numbers, multiply_numbers, convert_to_string]
)

result = Runner.run_sync(
    agent,
    "Add 10 and 5, multiply the result by 2, and convert the final answer to string",
    run_config=config
)

print(result.final_output)
