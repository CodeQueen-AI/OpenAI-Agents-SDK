from agents import Agent, Runner
from config import config

agent = Agent (
    name = 'CodeQueen Agent',
    instructions = 'You are a helpful assistant You are Task is to help the user with their Queries',
)

result = Runner.run_sync(agent,
                        'What is the Weather of the karachi?',
                        run_config=config)

print(result.final_output)