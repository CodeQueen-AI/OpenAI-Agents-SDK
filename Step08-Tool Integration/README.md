# 🤖 Tool Integration 

**Tool Integration** means:  
👉 "Connecting your agent with external logic or services (tools) so it can perform tasks it cannot do on its own."

🗣️ Urdu: Tool Integration ka matlab hai ke AI Agent kisi external tool ya service se connect ho kar usse kaam leta hai, jaise ke weather lana, currency conversion, ya language translation.


## ⚙️ Why Use Tools?

AI agents:
- ❌ don’t have real-time data
- ❌ can’t access personal or local data
- ❌ can’t run your custom logic

✅ So we **integrate tools** to give them that power!


## 🔄 Types of Tool Integration

OpenAI Agent SDK supports **3 types of tools**
## 1️⃣ HOSTED TOOLS

### 📌 What is it?

Prebuilt tools hosted by **OpenAI** (like Code Interpreter, DALL·E, or Browser). You just give the `tool_id`, and OpenAI manages the rest

### 🧪 Example:

```python
tool = {
    "type": "tool",
    "tool_id": "code_interpreter"  # hosted by OpenAI
}
````

### 📝 Explanation:

* You don’t write any code.
* You just tell the agent which **hosted tool** to use.
* Useful for advanced features (e.g., file analysis, image generation, etc.)

🗣️ Urdu: Ye tools already OpenAI ne banaye hote hain. Aap bas unka ID de kar use karte hain


## 2️⃣ FUNCTION TOOLS

### 📌 What is it?

You write a **Python function**, and your agent can use it like a tool

### 🧪 Example:

```python
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
```

### 📝 Explanation:

* You create a custom tool with Python
* Agent calls it when your prompt matches the tool’s purpose

🗣️ Urdu: Aap khud ka Python function likhte hain, aur agent use tool ki tarah use karta hai



## 3️⃣ AGENTS AS TOOLS

### 📌 What is it?

You convert one **Agent into a tool**, and another agent uses it like a helper

### 🧪 Example:

```python
from agents import Agent, Runner
from config import config

italian_agent = Agent(
    name='Italian Translator',
    instructions='Translate any English into Italian',
)

# Convert to tool
italian_tool = italian_agent.as_tool(
    tool_name='Translate_to_Italian',
    tool_description='Translate English to Italian'
)

# Main Agent
router = Agent(
    name='Router Agent',
    instructions='Use the Italian tool to translate.',
    tools=[italian_tool]
)

result = Runner.run_sync(router, "Translate 'I love learning' to Italian.", run_config=config)
print(result.final_output)
```

### 📝 Explanation:

* Aap ek agent ko tool banate ho.
* Dusra agent usko call karta hai jaise ek helper function

🗣️ Urdu: Aap ek agent ko helper bana ke dusre agent mein tool ki tarah use karte hain



## 📚 Summary Table

| Tool Type       | Purpose                                   | Who Makes It? | Example Task                    |
| --------------- | ----------------------------------------- | ------------- | ------------------------------- |
| Hosted Tool     | Prebuilt by OpenAI, just use tool\_id     | OpenAI        | Use code interpreter or browser |
| Function Tool   | Custom Python logic by user               | You           | Convert USD to PKR              |
| Agents as Tools | Use one agent as a tool for another agent | You           | Translate languages             |


## ✅ When to Use Which?

| Need                               | Use This Type |
| ---------------------------------- | ------------- |
| Built-in AI features (files, code) | Hosted Tool   |
| Custom logic / business rules      | Function Tool |
| Delegate task to sub-agents        | Agent as Tool |


