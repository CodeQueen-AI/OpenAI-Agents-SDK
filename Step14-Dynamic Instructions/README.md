Zaroor, Code Queen 👑! Neeche complete `README.md` file hai jo tumhare **Reusable Tools with Agents** project ke liye perfect hai. Ye file beginner-friendly hai aur har section explain karta hai simple language mein.

---

### 📄 `README.md`

````markdown
# 🤖 Reusable Tools with OpenAI Agents

This project demonstrates how to build **reusable tools** and connect them with **multiple agents** using the `openai-agents` SDK.

You’ll learn how to:
- Create tools that can be reused by different agents
- Add those tools to agents
- Run agents using the `Runner` class
- Understand how tool responses are used in multi-agent conversations

---

## 🔧 Technologies Used

- Python 🐍
- OpenAI Agents SDK
- Asyncio (for running async agent flows)

---

## 📁 Project Structure

```bash
project/
│
├── main.py          # Main script with agents and reusable tool
├── config.py        # OpenAI config (API key, model, etc.)
└── README.md        # You're reading it! 📘
````

---

## 📦 Installation

1. Clone the repo or copy the code
2. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install openai-agents
```

4. Add your API key to `config.py` like this:

```python
config = {
    "api_key": "sk-...",
    "model": "gpt-4o"  # or "gpt-4", "gpt-3.5-turbo"
}
```

---

## ✅ How It Works

### Reusable Tool

```python
@function_tool
def greet(name: str) -> str:
    return f"Hello, {name}! Welcome 😊"
```

Ye tool kisi bhi agent ke sath use ho sakta hai jise kisi ko greet karna ho.

---

### Agent 1: GreetBot

```python
agent1 = Agent(
    name="GreetBot",
    instructions="Greet the user by name.",
    tools=[greet]
)
```

Ye agent user ke naam se greet karta hai.

---

### Agent 2: WelcomeBot

```python
agent2 = Agent(
    name="WelcomeBot",
    instructions="Start responses with greetings.",
    tools=[greet]
)
```

Ye agent bhi greeting karta hai lekin slightly different instructions ke sath.

---

### Runner

```python
async def main():
    result1 = await Runner.run(starting_agent=agent1, input="Greet Sumbal", run_config=config)
    result2 = await Runner.run(starting_agent=agent2, input="Say hello to Zara", run_config=config)

    print("Agent 1 Output:", result1.final_output)
    print("Agent 2 Output:", result2.final_output)

asyncio.run(main())
```

Runner agents ko run karta hai aur unka response print karta hai.

---

## 🤔 Why Reusable Tools?

* Ek baar tool banao → multiple agents use kar sakte hain.
* Code DRY (Don't Repeat Yourself) rehta hai.
* Maintain karna easy hota hai.
* Scalability badhti hai (20+ agents use kar sakte hain same tool).

---

## 📌 Future Enhancements

* Add tools with dynamic input
* Use tools in chains (Agent A → Agent B)
* Store responses in a database

---

## 🧠 Learnings

✔ What are tools
✔ How to attach tools to agents
✔ How to reuse tools
✔ How to run agents with `Runner.run()`

---

## 👑 Created By

**Code Queen** with love and logic 💡

```

---

Agar tum chaho to is README ko GitHub par bhi paste kar sakti ho – it's ready to go 🚀

Kya tum chahogi ke mai ek aur README banaun jab tum dynamic instructions ya multi-tool chaining wala project complete karo?
```
