from agents import Agent , Runner
from config import config

agent = Agent(name="CodeQueenAgent", instructions="Respond in JSON when asked.")

def process_output(output_type):
    if output_type == "text":
        return "Hello, this is a text response!"
    elif output_type == "json":
        return {
            "message": "Hello, this is JSON response!",
            "status": "success"
        }

# Simulating agent output
print(process_output("text"))  # Text output
print(process_output("json"))  # JSON output
