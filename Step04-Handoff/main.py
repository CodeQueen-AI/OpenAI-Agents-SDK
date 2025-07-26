from agents import Agent, Runner
from config import config

# Math Agent
math_agent = Agent(
    name="Math Agent",
    handoff_description="Handles all math-related questions",
    instructions="Answer math questions in simple steps with one small example.",
)

# History Agent
history_agent = Agent(
    name="History Agent",
    handoff_description="Handles all history-related questions",
    instructions="Answer history questions briefly and clearly. Mention key dates or facts if needed.",
)

# Decision Agent
decision_agent = Agent(
    name="Decision Agent",
    instructions="Read the user's question and decide which agent should answer: Math Agent or History Agent.",
    handoffs=[
        history_agent,
        math_agent,
    ],
)

# Run it!
result = Runner.run_sync(
    decision_agent,
    "Who won the World War II?",  # Should be handled by History Agent
    run_config=config,
)

# Show the result
print("→", result.final_output)
