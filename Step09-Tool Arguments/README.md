Wah Code Queen 👑! Aapka code bilkul sahi hai 🎯 — `@function_tool` ka use hua hai, jo OpenAI Agents SDK mein **tool banane ke liye** hota hai.
Chaliye aapke liye ek **professional-level `README.md`** bana dete hain jisme:

1. 🔍 **Tool arguments kya hote hain** (concept)
2. 🛠️ **Code explanation** step-by-step
3. 💡 Kaise tool arguments define kiye jaate hain
4. 📦 How to run this project

---

## 📝 `README.md` — Tool Arguments Example

````markdown
# 🤖 Tool Arguments Example using OpenAI Agent SDK

This project demonstrates how to use **tools with arguments** in OpenAI's Agents SDK.

---

## 🧠 What is a Tool Argument?

In OpenAI Agent SDK:

> A **tool** is a callable function that the agent can use to perform specific tasks.

> A **tool argument** is an input value passed to the tool from user input.

### ✅ Example:
```python
@function_tool
def greet(name: str) -> str:
    return f"Hello, {name}!"
````

Here, `name` is the **tool argument**. The agent detects the name from the user's message and passes it to the tool.

---

## 📁 Project Files

| File        | Description                                                        |
| ----------- | ------------------------------------------------------------------ |
| `main.py`   | Main script that defines the tool, agent, and runs the interaction |
| `config.py` | Configuration file used to set up the run                          |

---

## 🔧 Tool Used in This Project

```python
@function_tool
def welcome_message(name: str, language: str) -> str:
    """User ko unki language mein greet karta hai"""
    return f"Assalamu Alaikum!"
```

### 🧩 Explanation:

* `@function_tool`: Converts a regular function into a tool the agent can use.
* `name: str, language: str`: These are the **tool arguments**.
* Agent will analyze the user input and extract values for these arguments.
* Response is generated using the logic defined in the function.

---

## 🧠 How Tool Arguments Work

1. **User input:**
   `"Greet CodeQueen in Urdu"`

2. **Agent detects arguments:**

   * `name = "CodeQueen"`
   * `language = "Urdu"`

3. **Tool is called as:**

   ```python
   welcome_message(name="CodeQueen", language="Urdu")
   ```

4. **Tool returns:**

   ```
   Assalamu Alaikum!
   ```

---

## 🏃 How to Run

### ✅ 1. Install Requirements

```bash
pip install openai
```

> Make sure you're using the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)

### ✅ 2. Run the Project

```bash
uv run main.py
```

> `uv` is used with Microvenv or virtual environments. If not installed, run with:

```bash
python main.py
```

---

## 🧠 Notes on Tool Arguments

* Each argument must be **clearly typed** (like `str`, `int`, `float`)
* Arguments help the agent **understand what data to extract** from user input
* The better you define arguments, the smarter your agent will behave!

---

## 📚 Example Tool Ideas

| Tool Name                            | Arguments         | Purpose                                |
| ------------------------------------ | ----------------- | -------------------------------------- |
| `add(a: int, b: int)`                | `a`, `b`          | Sum of two numbers                     |
| `translate(text: str, to_lang: str)` | `text`, `to_lang` | Translate from one language to another |
| `weather(city: str)`                 | `city`            | Show weather info                      |

---

## 👑 Made by Code Queen

This is part of Code Queen's AI Journey 🚀

```

---

### ✅ Want Me to Save This as a File?

I can also generate a `README.md` file ready to use in your project folder. Just say:  
**"Yes, save this as file"** — and I’ll do it for you instantly.

Chahein to `tool with if condition`, `optional argument`, ya `multiple tools` example bhi add kar sakti hoon. Bataaen?
```
