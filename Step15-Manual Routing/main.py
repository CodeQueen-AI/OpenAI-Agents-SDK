from agents import Agent, Runner
from config import config

# Two simple agents
support_agent = Agent(
    name="Support Agent",
    instructions="You help with customer support questions"
)

sales_agent = Agent(
    name="Sales Agent",
    instructions="You answer questions about products and prices"
)

# Manual routing logic
def manual_route(user_message):
    if "price" in user_message.lower() or "buy" in user_message.lower():
        return sales_agent
    else:
        return support_agent

# User message
message = "I want to know the price of this product."

# Decide manually which agent to use
chosen_agent = manual_route(message)

# Run the chosen agent
result = Runner.run_sync(chosen_agent, message , run_config=config)
print(result.final_output)
