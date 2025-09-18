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

# Forcing tool example
# Let's assume 'calculator' is a tool the agent can use
run_config_with_forcing = config.copy()
run_config_with_forcing['tools'] = ['calculator']  # Only calculator tool will be used

# Run the cloned agent with forcing tool
result = Runner.run_sync(
    cloned_agent,
    'What is the value of pi constant multiplied by 2?',
    run_config=run_config_with_forcing
)

print(result.final_output)
