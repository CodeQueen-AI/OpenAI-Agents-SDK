# Input Guardrails
from agents import Agent, Runner, RunContextWrapper
from config import config 
# Simple agent
info_agent = Agent(
    name="Info Agent",
    instructions="You answer basic questions."
)

# Guardrail: Sirf alphabets aur spaces allow
def input_guardrail(ctx: RunContextWrapper[str], agent: Agent) -> bool:
    text = ctx.context
    return text.replace(" ", "").isalpha()  # True agar sirf letters hain

# User ka message
user_message = "Hello World"

# Check guardrail
if input_guardrail(RunContextWrapper(user_message), info_agent):
    result = Runner.run_sync(info_agent, user_message , run_config=config)
    print(result.final_output)
else:
    print("❌ Invalid input. Only letters allowed.")





# Output Guardrails
from agents import Agent, Runner

# Simple agent
secret_agent = Agent(
    name="Secret Agent",
    instructions="Reply with a number: 12345"
)

# Output filter
def output_guardrail(output: str) -> str:
    if "12345" in output:
        return "⚠️ Sensitive info hidden."
    return output

# Run agent
result = Runner.run_sync(secret_agent, "Give me your number")
print(output_guardrail(result.final_output))
