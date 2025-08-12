## 🔁 **What is Reusable Tool?**

**English:**
A reusable tool is a function that is created once and can be used by multiple agents without rewriting it.

**Urdu:**
Reusable tool aik aisi function hoti hai jo sirf aik dafa banai jati hai, lekin use kai agents dobara-dobara istemal kar sakte hain — baar baar likhne ki zarurat nahi hoti.


## 📌 **Why do we use reusable tools?**

1. ✅ **Code reuse** – Ek hi tool ko multiple agents ya situations mein use kar sakte hain.
2. ✅ **Maintainable code** – Agar function mein koi change karna ho to sirf aik jaga update karna hota hai.
3. ✅ **Less duplication** – Har agent ke liye alag function likhne ki zarurat nahi.
4. ✅ **Consistency** – Sab agents same tarah se kaam karte hain, results consistent hotay hain


## 📆 **Kab banate hain reusable tool?**

**Jab ek hi function ko kai agents ya projects mein use karna ho.**
Jaise: greeting, calculation, formatting, etc.



## 🧠 **Kaise banate hain reusable tool?**

1. `@function_tool` decorator lagao.
2. Function define karo with clear input/output.
3. Us function ko multiple agents mein `tools=[...]` ke andar include karo.


## 🔍 **Code Explanation**

```python
from agents import Agent, Runner , function_tool
from config import config
import asyncio
```

* 🧠 **Agents, Runner, and function\_tool** ko import kiya.
* 🛠 `config` is used to run the agent properly.
* 🔁 `asyncio` for running the agents asynchronously (ek ke baad ek properly run karein).


### ✅ Reusable Tool Definition

```python
@function_tool
def greet(name: str) -> str:
    """User ka naam le kar greeting return karta hai."""
    return f"Hello, {name}! Welcome 😊"
```

* **Ye tool aik function hai** jo kisi bhi naam ko greet karta hai.
* `@function_tool` se OpenAI SDK is function ko tool bana deta hai.
* Input: `name`
  Output: Greeting string


### ✅ Agent 1: GreetBot

```python
agent1 = Agent(
    name="GreetBot",
    instructions="Greet the user by name.",
    tools=[greet]
)
```

* **Agent1** ka naam GreetBot hai.
* Iska kaam sirf greet karna hai using `greet` tool

  

### ✅ Agent 2: WelcomeBot

```python
agent2 = Agent(
    name="WelcomeBot",
    instructions="Start responses with greetings.",
    tools=[greet]
)
```

* **Agent2** bhi same `greet` tool use karta hai
* Dono agents alag hain, **but tool same** hai 


### ✅ Runner: Run both agents

```python
async def main():
    result1 = await Runner.run(
        starting_agent=agent1,
        input="Greet Sumbal",
        run_config=config
    )

    result2 = await Runner.run(
        starting_agent=agent2,
        input="Say hello to Zara",
        run_config=config
    )

    print("Agent 1 Output:", result1.final_output)
    print("Agent 2 Output:", result2.final_output)

asyncio.run(main())
```

* Dono agents **alag input** se run ho rahe hain:

  * `agent1` ko diya gaya: **"Greet Sumbal"**
  * `agent2` ko diya gaya: **"Say hello to Zara"**
* Output screen pe print ho raha hai:

```
Agent 1 Output: Hello, Sumbal! Welcome 😊
Agent 2 Output: Hello, Zara! Welcome 😊
```

> 🎯 **Result:** Ek hi `greet` tool dono agents ke liye **reuse** hua. Yehi hota hai **reusable tool**.



## 🏁 Summary

| Feature           | Explanation (Urdu + English)                            |
| ----------------- | ------------------------------------------------------- |
| Reusable Tool     | Aik hi dafa banai gayi function, kai jaga use hoti hai  |
| Kyun banate hain  | Code reuse, maintainability, consistency                |
| Kab banate hain   | Jab multiple agents ek hi function kaam karein          |
| Kaise banate hain | `@function_tool` use karo, aur agents mein include karo |
| Fayda kya hai?    | Fast development, less bugs, time saving                |


