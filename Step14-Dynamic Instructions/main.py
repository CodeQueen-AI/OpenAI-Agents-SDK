from agents import Agent, Runner
from config import config
import asyncio

# ✅ Dynamic Instruction generator
def generate_instruction(input_text: str) -> str:
    if "weather" in input_text.lower():
        return "Act like a weather reporter. Tell the weather details."
    elif "joke" in input_text.lower():
        return "Act like a comedian. Tell a funny joke."
    else:
        return "Act like a helpful assistant."

# ✅ Agent with dynamic instructions
async def main():
    user_input_1 = "Tell me a joke"
    user_input_2 = "What's the weather like?"

    # 🔄 Instructions change based on input
    agent1 = Agent(
        name="DynamicBot",
        instructions=generate_instruction(user_input_1)
    )
    
    agent2 = Agent(
        name="DynamicBot",
        instructions=generate_instruction(user_input_2)
    )

    result1 = await Runner.run(
        starting_agent=agent1,
        input=user_input_1,
        run_config=config
    )

    result2 = await Runner.run(
        starting_agent=agent2,
        input=user_input_2,
        run_config=config
    )

    print("Joke Response:", result1.final_output)
    print("Weather Response:", result2.final_output)

asyncio.run(main())
