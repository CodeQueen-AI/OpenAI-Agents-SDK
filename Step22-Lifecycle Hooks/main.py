from agents import Agent, Runner

# Agent ko define karo
agent = Agent(
    name="CodeQueenAgent",
    instructions="You are a helpful assistant."
)

# Agent lifecycle hook: on_start
def on_start():
    print("Agent has started!")

# Agent lifecycle hook: on_response
def on_response(response):
    print(f"Agent responded: {response}")

# Agent lifecycle hook: on_error
def on_error(error):
    print(f"Agent encountered an error: {error}")

# Attach lifecycle hooks
agent.on_start = on_start
agent.on_response = on_response
agent.on_error = on_error

# Simulate running a task
agent.on_start()
agent.on_response("Hello, how can I assist you today?")
agent.on_error("Network timeout error.")
