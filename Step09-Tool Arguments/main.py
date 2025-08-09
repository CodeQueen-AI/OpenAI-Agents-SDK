from agents import Agent, Runner, function_tool
from config import config

@function_tool
def welcome_message(name: str, language: str) -> str:
    """User ko unki language mein greet karta hai"""
    return f"Assalamu Alaikum!"

agent = Agent(
    name="Greeting Agent",
    instructions="Greet the user based on their name and preferred language. Use the tool.",
    tools=[welcome_message]  
)

result = Runner.run_sync(
    agent,
    "Greet CodeQueen in Urdu", 
    run_config=config
)

print(result.final_output)
