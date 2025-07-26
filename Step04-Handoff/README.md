### 🧠 What is a Handoff?

**Handoff** means giving control of the user's question to another agent who is **more suitable** for answering that specific type of question.

For example:

> If a user asks a **math question**, the **Decision Agent** will *hand off* the question to the **Math Agent**


### 🔄 `handoff` vs `handoffs`

| Keyword    | Meaning                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------- |
| `handoff`  | Used inside an agent's **response**, when it decides to **send** the question to another agent. |
| `handoffs` | A list of agents that this agent is **allowed** to hand off to.                                 |

> ✅ In this code, `decision_agent` uses `handoffs=[math_agent, history_agent]` to define which agents it can forward to.



### 🧩 Code Explanation (Line by Line)

```python
from agents import Agent, Runner
from config import config
```

* ✅ **Importing** the required tools:

  * `Agent`: lets us create AI agents.
  * `Runner`: helps run agents.
  * `config`: contains API settings (like keys, etc.)


```python
# Math Agent
math_agent = Agent(
    name="Math Agent",
    handoff_description="Handles all math-related questions",
    instructions="Answer math questions in simple steps with one small example.",
)
```

* ✅ Creating a **Math Agent**
* Handles questions related to **math**
* Instruction: explain step by step and include a small example


```python
# History Agent
history_agent = Agent(
    name="History Agent",
    handoff_description="Handles all history-related questions",
    instructions="Answer history questions briefly and clearly. Mention key dates or facts if needed.",
)
```

* ✅ Creating a **History Agent**
* Handles **history-related** questions
* Responds briefly, with important dates/facts if necessary


```python
# Decision Agent
decision_agent = Agent(
    name="Decision Agent",
    instructions="Read the user's question and decide which agent should answer: Math Agent or History Agent.",
    handoffs=[
        history_agent,
        math_agent,
    ],
)
```

* ✅ Creating a **Decision Agent**
* This is the **main agent** that reads any question
* It decides whether to send the question to the **Math Agent** or the **History Agent**
* It can only *handoff* to the two agents listed in `handoffs`


```python
# Run it!
result = Runner.run_sync(
    decision_agent,
    "Who won the World War II?",  # Should be handled by History Agent
    run_config=config,
)
```

* ✅ Running the **Decision Agent** synchronously
* Input: `"Who won the World War II?"`
* Based on question type, it will **handoff** to the **History Agent**


```python
# Show the result
print("→", result.final_output)
```

* ✅ Print the final output of the agent chain
* This shows the **actual answer** from the agent who handled the question



### 🧪 Example Output

```
→ The Allies won World War II in 1945, defeating the Axis powers
```


### ✅ Summary

* We created 3 agents:

  * 🔢 Math Agent
  * 📜 History Agent
  * 🤖 Decision Agent
* **Decision Agent** chooses the right expert based on the question
* **Handoff** allows smart delegation
* `handoffs` list defines who an agent can hand over to

