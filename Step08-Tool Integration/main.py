# Function Tools
from agents import Agent , Runner , function_tool
from config import config

@function_tool
def usd_to_pkr():
    return 'Today USD to PKR is 200'

agent = Agent(
    name = 'General Agent',
    instructions = 'You are a helpful Assistant',
    tools=[usd_to_pkr]
)

result = Runner.run_sync(agent,
                         'What is USD to PKR today?',
                         run_config=config)

print(result.final_output)


# Agents as Tool
from agents import Agent, Runner
from config import config

italian_agent = Agent(
    name='Italian Translator',
    instructions='Translate any English into Italian',
)

spanish_agent = Agent(
    name='Spanish Translator',
    instructions='Translate any English into Spanish',
)

french_agent = Agent(  # small 'f'
    name='French Translator',
    instructions='Translate any English into French',
)

# Main Router Agent
translation_router = Agent(
    name='Translation Router',
    instructions="""You are a translation assistant. Route the translation request to the correct language agent.
    Use the appropriate tool to convert English text into Italian, Spanish, or French based on the request.""",
    tools=[
        italian_agent.as_tool(
            tool_name='Translate_to_Italian',
            tool_description='Translate the user\'s message to Italian'
        ),
        spanish_agent.as_tool(
            tool_name='Translate_to_Spanish',
            tool_description='Translate the user\'s message to Spanish'
        ),
        french_agent.as_tool(
            tool_name='Translate_to_French',
            tool_description='Translate the user\'s message to French'
        ),
    ]
)

result = Runner.run_sync(italian_agent, "Translate 'I love learning' into italian.", run_config=config)
print(result.final_output)
