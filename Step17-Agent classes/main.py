from agents import Agent, Runner
from config import config

# Create a custom agent class 
class MyBankAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Bank Agent",
            instructions="You answer balance and bank-related queries."
        )

# Use the custom class
bank_agent = MyBankAgent()

# Run the agent
result = Runner.run_sync(bank_agent, "What is my balance?" , run_config=config)
print(result.final_output)
