Bilkul Code Queen! Neeche maine ek **simple aur beginner-friendly README file** likhi hai jo `Tool Calling`, `Non-Real-Time`, `Real-Time`, aur `Personalized Data` ko explain karti hai. Ye same code jo aapne diya usko bhi use kiya gaya hai examples mein. Aap is README.md ko apne project folder mein rakh sakti hain.

---

### ✅ `README.md`

````markdown
# 🛠️ Tool Calling in Agents (OpenAI SDK)

## 🔍 What is Tool Calling?

**Tool Calling** is a feature that allows an AI agent to connect with external tools (like APIs, databases, weather services, etc.) to get answers that it cannot generate on its own.

### ✅ Why do we use Tool Calling?

Sometimes AI doesn't have:
- Live updates
- Personal data access
- Recent information

So, it uses **Tool Calling** to get that data from external sources.

---

## 🧠 How It Works?

1. An **Agent** is created (a helpful assistant).
2. We give the agent a **query** (a question).
3. Agent uses **Runner.run_sync()** to call tools and get the answer.
4. The final result is printed.

---

## 🔄 Types of Tool Calling (Based on Data):

### 1. 📜 Non-Real-Time Data (Historical Data)
**Definition:** Data that does not change. It is already known or stored before (like history facts).

**Example Code:**
```python
from agents import Agent , Runner
from config import config

agent = Agent(
    name = 'General Agent',
    instructions = 'You are a helpful Assistant'
)

result = Runner.run_sync(agent,
                         'Who is the Founder of Pakistan',
                         run_config=config)

print(result.final_output)
````

---

### 2. 🌦 Real-Time Data (Current Live Data)

**Definition:** Data that is constantly updating, like weather or news.

**Example Code:**

```python
from agents import Agent , Runner
from config import config

agent = Agent(
    name = 'General Agent',
    instructions = 'You are a helpful Assistant'
)

result = Runner.run_sync(agent,
                         'What is the Weather of The Karachi?',
                         run_config=config)

print(result.final_output)
```

---

### 3. 🙋 Personalized Data (User-Specific Data)

**Definition:** Data related to a person, user, or organization. It’s private and specific.

**Example Code:**

```python
from agents import Agent , Runner
from config import config

agent = Agent(
    name = 'General Agent',
    instructions = 'You are a helpful Assistant'
)

result = Runner.run_sync(agent,
                         'Show me the top 10 students of class 9?',
                         run_config=config)

print(result.final_output)
```

---

## 📌 Summary

| Type               | Meaning                       | Example                 |
| ------------------ | ----------------------------- | ----------------------- |
| Non-Real-Time Data | Past facts, historical data   | Founder of Pakistan     |
| Real-Time Data     | Live updates                  | Weather of Karachi      |
| Personalized Data  | Private or specific user data | Top students of a class |

---

## 🧪 Tools Involved

* `Agent` – defines the assistant.
* `Runner.run_sync()` – runs the tool calling process.
* `config` – contains tool setup and configurations.

---

> 👑 Made for learning and practice by **Code Queen**

```

---

Aap chaahein to is README file ko `README.md` ke naam se save kar ke GitHub par upload bhi kar sakti hain.  
Agar aap chaahein to main isko **further beautify** bhi kar sakta hoon headings, emojis ya badges ke sath. Let me know!
```
