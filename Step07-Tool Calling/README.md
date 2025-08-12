# 🛠️ Tool Calling in Agents 
**Tool Calling** is a feature that allows an AI agent to connect with external tools (like APIs, databases, weather services, etc.) to get answers that it cannot generate on its own.

### ✅ Why do we use Tool Calling?

Sometimes AI doesn't have:
- Live updates
- Personal data access
- Recent information

So, it uses **Tool Calling** to get that data from external sources

## 🧠 How It Works?

1. An **Agent** is created (a helpful assistant)
2. We give the agent a **query** (a question)
3. Agent uses **Runner.run_sync()** to call tools and get the answer
4. The final result is printed


## 🔄 Types of Tool Calling (Based on Data):

### 1. 📜 Non-Real-Time Data (Historical Data)
**Definition:** Data that does not change. It is already known or stored before (like history facts).


### 2. 🌦 Real-Time Data (Current Live Data)

**Definition:** Data that is constantly updating, like weather or news


### 3. 🙋 Personalized Data (User-Specific Data)

**Definition:** Data related to a person, user, or organization. It’s private and specific


## 📌 Summary

| Type               | Meaning                       | Example                 |
| ------------------ | ----------------------------- | ----------------------- |
| Non-Real-Time Data | Past facts, historical data   | Founder of Pakistan     |
| Real-Time Data     | Live updates                  | Weather of Karachi      |
| Personalized Data  | Private or specific user data | Top students of a class |


## 🧪 Tools Involved

* `Agent` – defines the assistant
* `Runner.run_sync()` – runs the tool calling process
* `config` – contains tool setup and configurations
