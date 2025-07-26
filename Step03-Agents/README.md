### 🔰 What is an Agent?

An **Agent** is a smart assistant designed to follow specific instructions and complete tasks, like answering questions, solving problems, or making decisions

**Example:**
If you tell an agent: *"Translate this text"* — it will follow your instructions and return the translation


### ⚙️ How Do Agents Work?

Agents work in 3 simple steps:

1. **Define** what the agent should do (using instructions)
2. **Run** the agent on a task or question
3. **Get the result** returned by the agent

In Python, this is handled using classes like `Agent`, `Runner`, and a `config` for settings (like API keys, model settings, etc.)

### 🧩 Code Explained — Line by Line

```python
from agents import Agent, Runner
```

📦 This line imports the `Agent` and `Runner` classes from the `agents` library

* **Agent** is used to create a smart assistant
* **Runner** is used to execute the agent with input


```python
from config import config
```

🛠 This imports a `config` object from your config file
It usually contains:

* API key
* Model name
* Tool settings
* Streaming preferences
  (You must create or edit this `config.py` file yourself.)



```python
agent = Agent (
    name = 'CodeQueen Agent',
    instructions = 'You are a helpful assistant You are Task is to help the user with their Queries',
)
```

🤖 This creates an **Agent** called `"CodeQueen Agent"` with instructions.

* `name`: A name to identify your agent
* `instructions`: What the agent should do. Here, the agent is told to **"help the user with their queries"**



```python
result = Runner.run_sync(agent,
                        'What is the Weather of the karachi?',
                        run_config=config)
```

🚀 This line runs your agent **synchronously** (in blocking mode)

* `Runner.run_sync(...)` means: run this agent **immediately and wait** for its response
* `'What is the Weather of the karachi?'` is the user’s question
* `run_config=config` passes all necessary settings to the agent



```python
print(result.final_output)
```

🖨 This line prints the **final output** returned by the agent
You’ll see the response on your terminal like:
`"The weather in Karachi is hot and humid today"`



### 🗂 Project Structure Example

```
📁 project-folder/
│
├── config.py             # Your config file (contains model/API settings)
├── main.py               # Your main agent code 
└── README.md             # This guide
```
