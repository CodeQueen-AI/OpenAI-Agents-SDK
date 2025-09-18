from agents import Agent, Runner
from config import config

# Original agent
agent = Agent(
    name='CodeQueen Agent',
    instructions='You are a helpful assistant. Your task is to help the user with their queries',
)

# Cloned agent with modified instructions
cloned_agent = agent.clone(
    name='CodeQueen Expert Agent',
    instructions='You are an expert assistant. Provide detailed and advanced answers to the user.'
)

# Run the cloned agent
result = Runner.run_sync(
    cloned_agent,
    'What is the value of the pie constant?',
    run_config=config
)

print(result.final_output)
