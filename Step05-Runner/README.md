### 🧠 What is `Runner`?

`Runner` is a helper class that is used to **run or execute an Agent**.
Aapka `Agent` instructions deta hai, lekin us Agent ko chalane ka kaam `Runner` karta hai.

Think of it like this

| Role     | Meaning                                   |
| -------- | ----------------------------------------- |
| `Agent`  | Thinker (Instructions and name)           |
| `Runner` | Doer (Executes the Agent with user input) |


### 🔧 How does `Runner` work?

1. `Runner` takes:

   * Your `Agent`
   * User input (prompt)
   * `config` (optional settings)

2. It gives you:

   * A **final output** (answer from the agent)

### 🛠️ Runner Methods

Runner ke do tarike ke methods hote hain:

| Method       | Type         | Used when...                              |
| ------------ | ------------ | ----------------------------------------- |
| `run_sync()` | Synchronous  | You want to run normally, without `async` |
| `run()`      | Asynchronous | You want to use `async` features          |


## 🔁 1. Synchronous Runner – `run_sync()`

Ye normal function ki tarah kaam karta hai, `await` use nahi hota.

### ✅ Code Example:

```python
from agents import Agent, Runner
from config import config

agent = Agent(
    name="Sync Agent",
    instructions="Give short and correct answers."
)

result = Runner.run_sync(
    agent,
    "What is 5 * 10?",
    run_config=config
)

print(result.final_output)
```

### 🔍 Output:

```
50
```


## ⚡ 2. Asynchronous Runner – `run()`

Ye method `async/await` ke sath chalta hai. Ye useful hai jab aap background mein tasks run karna chahtay hain ya real-time systems mein kaam kar rahe ho

### ✅ Code Example:

```python
import asyncio
from agents import Agent, Runner
from config import config

agent = Agent(
    name="Async Agent",
    instructions="Be helpful and friendly."
)

async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="What is the capital of Pakistan?",
        run_config=config
    )
    print(result.final_output)

# Start async process
asyncio.run(main())
```

### 🔍 Output:

```
Islamabad
```

## 🔄 Async vs Sync: Key Differences

| Feature       | Sync (`run_sync`)     | Async (`run`)                     |
| ------------- | --------------------- | --------------------------------- |
| Blocking      | Yes                   | No                                |
| Uses `await`? | ❌                     | ✅                                 |
| Performance   | Slower in multi-tasks | Faster in multi-task environments |
| Ideal for...  | Simple scripts        | Real-time apps, web servers, etc. |



## 📌 Summary

* `Runner` executes the logic of your `Agent`
* Two methods:
  ✅ `run_sync()` — easy, blocking, direct
  ✅ `run()` — powerful, async, best for advanced apps
* Use `run_sync()` for beginners and small tasks
* Use `run()` if you're working with web apps, background tasks, or want full async control
