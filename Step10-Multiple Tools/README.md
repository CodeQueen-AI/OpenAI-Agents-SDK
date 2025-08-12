# 🧠 Multiple Tools – Calculator Agent

## 📌 What Are Multiple Tools?

Using different tools together to perform various tasks or solve problems

### ✅ Why Use Multiple Tools?

We use **multiple tools** when:

* We want the agent to handle **more than one task**.
* Each tool solves a **specific part of the problem**.
* Tools make the agent **modular, reusable**, and easy to manage.


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

## 🤖 Agent Setup

```python
agent = Agent(
    name="Calculator Agent",
    instructions="You are a helpful Assistant",
    tools=[add_numbers, multiply_numbers, convert_to_string]
)
```

> 🧠 **Explanation**:
> We give the agent 3 tools — add, multiply, and convert — so it can use them **in sequence** if needed


## 🚀 Running the Agent

```python
result = Runner.run_sync(
    agent,
    "Add 10 and 5, multiply the result by 2, and convert the final answer to string",
    run_config=config
)
```

## 🖨 Output

```python
print(result.final_output)
```


## 🔍 Step-by-Step Execution

| Step | Description              | Tool Used           | Result |
| ---- | ------------------------ | ------------------- | ------ |
| 1    | Add 10 and 5             | `add_numbers`       | 15     |
| 2    | Multiply 15 by 2         | `multiply_numbers`  | 30     |
| 3    | Convert 30 into a string | `convert_to_string` | "30"   |


## 💡 Summary

* Tools are like **functions** your agent can use
* You can add **multiple tools** to perform **complex operations**
* The agent chooses which tool to call based on your **natural language prompt**
* It’s **automatic chaining** — you don’t need to call the tools manually
