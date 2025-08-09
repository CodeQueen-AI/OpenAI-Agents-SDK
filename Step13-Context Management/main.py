# # LLM Context
from agents import Agent , Runner
from config import config
import asyncio

agent = Agent(
    name = 'Polite Assistant',
    instructions = 'User ka name Codequeen hai Humehsa polite raho aur har jawab mei "codequeen" keh kr pukaro' 
)

async def main(): 
    result = await Runner.run(
        starting_agent=agent,
        input='Who is the founder of Pakistan?',
        run_config=config
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

# Local Context
# from agents import Agent , Runner , function_tool , RunContextWrapper
# import asyncio
# from config import config
# from dataclasses import dataclass

# @dataclass
# class UserInfo:
#     name : str
#     uid : int

# @function_tool
# async def fetch_user_age(wrapper : RunContextWrapper[UserInfo]) -> str:
#     return f" {wrapper.context.name} User is 25 Years Old."

# async def main():
#     user_info = UserInfo(name='CodeQueen' , uid=101)

#     agent = Agent[UserInfo](
#         name='Assistant',
#         tools=[fetch_user_age]
#     )

