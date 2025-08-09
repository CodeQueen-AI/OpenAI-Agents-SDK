from agents import Agent, Runner
from config import config

# Agent create karo
agent = Agent(
    name="CodeQueenAgent",
    instructions="You are a helpful assistant"
)

# Event handlers define karo
def on_start(agent):
    print(f"{agent.name} started working!")

def on_response(agent, response):
    print(f"{agent.name} responded: {response}")

def on_error(agent, error):
    print(f"{agent.name} error: {error}")

# Normally aap events ko subscribe karoge SDK ke methods se,
# but yahan simple example hai:

agent.on_start = lambda: on_start(agent)
agent.on_response = lambda response: on_response(agent, response)
agent.on_error = lambda error: on_error(agent, error)

# Simulate running a task
agent.on_start()
agent.on_response("Hello, how can I help you today?")
agent.on_error("Network error occurred.")
