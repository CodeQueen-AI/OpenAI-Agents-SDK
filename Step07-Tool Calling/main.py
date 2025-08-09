# Tool Calling
# Non Real Time Data (Historical Data)
from agents import Agent , Runner
from config import config

agent = Agent(
    name = 'General Agent',
    instructions = 'You are a helpful Assistant'
)

result = Runner.run_sync(agent,
                         'Who is the Founder of Pakistan',
                         run_config=config)

print(result.final_output)


# Real Time Data (Current Update)
from agents import Agent , Runner
from config import config

agent = Agent(
    name = 'General Agent',
    instructions = 'You are a helpful Assistant'
)

result = Runner.run_sync(agent,
                         'What is the Weather of The karachi?',
                         run_config=config)

print(result.final_output)


# Personalized Data (Personal Information)
from agents import Agent , Runner
from config import config

agent = Agent(
    name = 'General Agent',
    instructions = 'You are a helpful Assistant'
)

result = Runner.run_sync(agent,
                         'Show me the top 10 students of class 9?',
                         run_config=config)

print(result.final_output)