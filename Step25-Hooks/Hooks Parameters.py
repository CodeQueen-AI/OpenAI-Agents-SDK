# app_hooks_demo.py

from agents import Agent, Runner, RunContextWrapper, AgentHooks
from pydantic import BaseModel
from dataclasses import dataclass
from typing import Any
from rich import print
from rich.panel import Panel
import asyncio

# 🔹 Custom context
class MyContext(BaseModel):
    user: str

# 🔹 Tools
def greet(ctx: RunContextWrapper[MyContext]) -> str:
    return f"👋 Hello [bold blue]{ctx.context.user}[/bold blue]!"

def farewell(ctx: RunContextWrapper[MyContext]) -> str:
    return f"👋 Goodbye [bold magenta]{ctx.context.user}[/bold magenta]!"

# 🔹 Agent A Hooks
@dataclass
class AgentAHooks(AgentHooks[MyContext]):
    async def on_start(self, context: RunContextWrapper[MyContext], agent: Agent[MyContext]) -> None:
        print(f"[green]🚀 {agent.name} Started for {context.context.user}[/green]")

    async def on_end(self, context: RunContextWrapper[MyContext], agent: Agent[MyContext], output: Any) -> None:
        print(f"[green]✅ {agent.name} Ended with output: {output.final_output}[/green]")

    async def on_handoff(self, context: RunContextWrapper[MyContext], from_agent: Agent[MyContext], to_agent: Agent[MyContext]) -> None:
        print(f"[yellow]🤝 Handoff from {from_agent.name} to {to_agent.name}[/yellow]")

# 🔹 Agent B Hooks
@dataclass
class AgentBHooks(AgentHooks[MyContext]):
    async def on_start(self, context: RunContextWrapper[MyContext], agent: Agent[MyContext]) -> None:
        print(f"[red]🚀 {agent.name} Started[/red]")

    async def on_end(self, context: RunContextWrapper[MyContext], agent: Agent[MyContext], output: Any) -> None:
        print(f"[red]✅ {agent.name} Ended with output: {output.final_output}[/red]")

# 🔹 Agents (No real OpenAI model here for simplicity, using mock responses)
agent_a = Agent(
    name="Agent A",
    instructions="Greet the user and hand off to Agent B.",
    tools=[greet],
    hooks=AgentAHooks()
)

agent_b = Agent(
    name="Agent B",
    instructions="Say goodbye to the user.",
    tools=[farewell],
    hooks=AgentBHooks()
)

# 🔹 Runner setup
runner = Runner(
    agents=[agent_a, agent_b],
    max_steps=5
)

# 🔹 Main async function
async def main():
    ctx = MyContext(user="CodeQueen")
    result = await runner.run(
        input="Start conversation",
        context=ctx
    )
    print(Panel.fit(str(result), title="🏁 Final Result"))

# 🔹 Run app
if __name__ == "__main__":
    asyncio.run(main())
