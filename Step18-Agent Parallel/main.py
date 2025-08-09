from agents import Agent, Runner
from config import config

# Two simple agents
weather_agent = Agent(
    name="Weather Agent",
    instructions="Give today's weather."
)

news_agent = Agent(
    name="News Agent",
    instructions="Give today's headline."
)

# Run both agents in parallel
results = Runner.run_parallel_sync(
    [
        (weather_agent, "What's the weather today?"),
        (news_agent, "What's the latest news?")
    ],
    run_config=config
)

# Show results
for r in results:
    print(r.final_output)
