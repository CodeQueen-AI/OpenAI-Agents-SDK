Here’s a complete `README.md` file for your **Multiple Tools Example** using OpenAI Agent SDK with **step-by-step explanation**, purpose, and deep understanding.

---

# 🧠 Multiple Tools in OpenAI Agent SDK – Calculator Agent

This example demonstrates how to **define and use multiple tools** inside a single agent using the OpenAI Agent SDK. You’ll learn what tools are, why we use them, and how they work together to solve a complex task step-by-step.

---

## 📌 What Are Tools?

In the OpenAI Agent SDK, **tools are functions** that the agent can call to perform specific tasks.
They are declared using `@function_tool` and added to the agent using the `tools=[...]` list.

### ✅ Why Use Multiple Tools?

We use **multiple tools** when:

* We want the agent to handle **more than one task**.
* Each tool solves a **specific part of the problem**.
* Tools make the agent **modular, reusable**, and easy to manage.

---

## 🧮 Example: Calculator Agent with 3 Tools

### 🔧 Tools Used

```python
@function_tool
def add_numbers(a: int, b: int) -> int:
    """Do numbers ka sum return karta hai.""" 
    return a + b
```

```python
@function_tool
def multiply_numbers(a: int, b: int) -> int:
    """Do numbers ka product return karta hai."""
    return a * b
```

```python
@function_tool
def convert_to_string(value: int) -> str:
    """Number ko string mein convert karta hai."""
    return str(value)
```

---

## 🤖 Agent Setup

```python
agent = Agent(
    name="Calculator Agent",
    instructions="You are a helpful Assistant",
    tools=[add_numbers, multiply_numbers, convert_to_string]
)
```

> 🧠 **Explanation**:
> We give the agent 3 tools — add, multiply, and convert — so it can use them **in sequence** if needed.

---

## 🚀 Running the Agent

```python
result = Runner.run_sync(
    agent,
    "Add 10 and 5, multiply the result by 2, and convert the final answer to string",
    run_config=config
)
```

> ✍️ **Prompt Explanation**:
> Agent ko yeh bola gaya hai:

1. **Add 10 and 5 →** Result: 15
2. **Multiply result (15) × 2 →** Result: 30
3. **Convert 30 to string →** Result: `"30"` (as a string)

---

## 🖨 Output

```python
print(result.final_output)
```

> ✅ **Expected Output**:

```
"30"
```

---

## 🔍 Step-by-Step Execution

| Step | Description              | Tool Used           | Result |
| ---- | ------------------------ | ------------------- | ------ |
| 1    | Add 10 and 5             | `add_numbers`       | 15     |
| 2    | Multiply 15 by 2         | `multiply_numbers`  | 30     |
| 3    | Convert 30 into a string | `convert_to_string` | "30"   |

---

## 💡 Summary

* Tools are like **functions** your agent can use.
* You can add **multiple tools** to perform **complex operations**.
* The agent chooses which tool to call based on your **natural language prompt**.
* It’s **automatic chaining** — you don’t need to call the tools manually.

---

## 🧠 Pro Tip

Want to build more advanced agents? Just add more tools like:

* `subtract_numbers`
* `divide_numbers`
* `check_even_or_odd`
* `convert_to_binary`
* `log_result`

---

If you’d like, I can help you convert this into an actual `.md` file and share it as a downloadable or GitHub-ready version.

Would you like that, Code Queen? 👑
