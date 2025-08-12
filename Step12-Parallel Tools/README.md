## 🚀 What are Parallel Tools?

**Parallel tools** are tools that can be used by an agent **together** during a single run — instead of one tool being called at a time, the agent decides to **use many tools in parallel** to give a better, faster, or more complete answer.


## ✅ Why Use Parallel Tools?

| Benefit     | Explanation                                                       |
| ----------- | ----------------------------------------------------------------- |
| ⏱️ Faster   | Multiple tools run side-by-side, saving time.                     |
| 🧠 Smarter  | Agent can use different types of tools to give a deeper response. |
| 🔁 Reusable | Tools can be shared across multiple agents.                       |


## 🧠 How It Works?

When the user gives input like:

> "Tell me the time and also greet Zara"

The agent decides:

* 🧭 Use the `get_time()` tool to get the current time.
* 🙋‍♀️ Use the `greet(name)` tool to greet Zara.

These tools **run in parallel**, and then the agent combines both results into one final output


## 🔍 Explanation

| Part              | What It Does                                |
| ----------------- | ------------------------------------------- |
| `greet(name)`     | Custom function to greet a user by name.    |
| `get_time()`      | Returns the current time.                   |
| `Agent`           | Uses both tools to reply to complex inputs. |
| `Runner.run(...)` | Runs the agent and gets the output.         |

## 📌 When to Use Parallel Tools?

Use parallel tools when:

* You want multiple actions done in one request.
* The user input involves **two or more goals**.
* Tools are independent of each other


