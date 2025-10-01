from agents import Agent, Runner
from config import config

def before_run_hook(input_text):
    print("Before Run Hook Triggered!")
    print("Input:", input_text)
    # Modify input if needed
    return input_text + " Please answer briefly"

def after_run_hook(result):
    print("After Run Hook Triggered!")
    print("Output:", result.final_output)
    return result

agent = Agent(
    name='CodeQueen Agent',
    instructions='You are a helpful assistant',
    hooks={
        "on_before_run": before_run_hook,
        "on_after_run": after_run_hook
    }
)

result = Runner.run_sync(agent, "What is the value of pi constant?", run_config=config)
print(result.final_output)

