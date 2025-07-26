from agents import Agent, Runner
from config import config

agent = Agent (
    name = 'CodeQueen Agent',
    instructions = 'You are a helpful assistant You are Task is to help the user with their Queries',
)

result = Runner.run_sync(agent,
                        'What is the value of the pie constant?',
                        run_config=config)

print(result.final_output)
