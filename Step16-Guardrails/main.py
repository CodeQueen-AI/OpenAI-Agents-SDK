# Input Guardrails
from agents import Agent, Runner, RunContextWrapper

# Simple agent
info_agent = Agent(
    name="Info Agent",
    instructions="You answer basic questions."
)

# Guardrail: Only allow short messages
def input_guardrail(ctx: RunContextWrapper[str], agent: Agent) -> bool:
    return len(ctx.context) <= 20  # Max 20 characters

# User input
user_message = "Tell me about the bank"

# Check before running
if input_guardrail(RunContextWrapper(user_message), info_agent):
    result = Runner.run_sync(info_agent, user_message)
    print(result.final_output)
else:
    print("❌ Input too long. Please make it shorter.")



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
