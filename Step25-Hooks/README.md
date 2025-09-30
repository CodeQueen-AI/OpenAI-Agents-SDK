# 🔹 OpenAI Agents SDK – Hooks

**Hooks** are a mechanism that lets you **run custom logic at specific points in an agent’s lifecycle**. They allow you to add **extra functionality** without changing the agent’s core behavior.


## 1️⃣ What Are Hooks?

* Hooks are like **callback functions** that trigger automatically.
* They run at **specific events** during the agent’s lifecycle.
* Example: before the agent runs, after it produces output, or when it calls a tool.

**Purpose of Hooks:**

* Inspect or modify input
* Inspect, log, or modify output
* Monitor agent behavior and gather analytics
* Handle errors gracefully


## 2️⃣ Types of Hooks

1. **Before Run Hook (`on_before_run`)**

   * Runs **before the agent executes**.
   * Use cases:

     * Modify input (e.g., “Answer briefly” instruction)
     * Log input for tracking
     * Validate input

2. **After Run Hook (`on_after_run`)**

   * Runs **after the agent finishes execution**.
   * Use cases:

     * Inspect agent output
     * Modify output if needed
     * Log responses or gather analytics

3. **On Tool Call Hook (`on_tool_call`)**

   * Triggered when the agent uses a tool.
   * Use cases:

     * Track tool usage
     * Restrict or customize tool usage

4. **On Handoff Hook (`on_handoff`)**

   * Triggered when one agent **hands off a task to another agent**.
   * Use cases:

     * Track workflow transitions
     * Send notifications or trigger automation

5. **On Error Hook (`on_error`)**

   * Triggered if the agent throws an error during execution.
   * Use cases:

     * Custom error handling
     * Alert generation


## 3️⃣ Hooks Parameters

Hooks come with **parameters** that give you **access to agent and context information**:

| Hook Name       | Parameter           | Purpose / Use Case                                                             |
| --------------- | ------------------- | ------------------------------------------------------------------------------ |
| `on_before_run` | `input_text`        | Access or modify the input question before the agent runs.                     |
| `on_after_run`  | `result`            | Inspect or modify the agent’s output after execution.                          |
| `on_tool_call`  | `tool_name`         | Track or control which tools the agent uses.                                   |
| `on_handoff`    | `from_agent`        | Identify which agent completed the task.                                       |
|                 | `to_agent`          | Identify which agent received the task.                                        |
| `on_error`      | `exception`         | Handle errors gracefully and take custom actions.                              |
| `context`       | `RunContextWrapper` | Access user data, session info, or other custom variables for the current run. |

**Notes:**

* `context` gives access to **custom user data** like username, session info, and variables.
* `agent` gives access to **agent properties**, tools, and instructions.
* `result/output` lets you inspect **final agent output**.
* `from_agent` & `to_agent` help track **handoffs in multi-agent workflows**.


## 4️⃣ Hooks Flow

1. **Input Stage** → `on_before_run` triggers → input is inspected/modified
2. **Agent Execution** → agent performs its task
3. **Output Stage** → `on_after_run` triggers → output is inspected/modified
4. **Handoff Stage (optional)** → `on_handoff` triggers
5. **Error Handling** → `on_error` triggers if there’s an exception

**Conceptual Flow Diagram:**

```
User Input → [on_before_run] → Agent Execution → [on_tool_call] → [on_after_run] → [on_handoff] → Final Output
```


## 5️⃣ Benefits of Using Hooks

* ✅ **Custom Behavior** – Modify input/output dynamically.
* ✅ **Monitoring & Logging** – Track what the agent received and returned.
* ✅ **Validation** – Ensure inputs and outputs are correct and safe.
* ✅ **Automation** – Automate workflows, multi-agent handoffs, or notifications.
* ✅ **Error Handling** – Gracefully handle errors and alert administrators.


## 6️⃣ Real-World Use Cases

1. **Customer Support Agent**

   * Input: Customer query
   * `on_before_run`: Sanitize input or add context
   * `on_after_run`: Log response for analytics

2. **Multi-Agent Workflow**

   * Agent A completes a task → `on_handoff` → Agent B continues task
   * Track which agent did what

3. **Calculator Tool Enforcement**

   * `on_tool_call`: Ensure the agent only uses a calculator tool for math queries

4. **Error Alerts**

   * `on_error`: Send notifications if the agent fails


## 7️⃣ Key Takeaways

* Hooks in OpenAI Agents SDK **extend agent functionality without changing core logic**.
* Parameters provide **full context and control** over agent execution.
* Using hooks properly allows you to **monitor, validate, automate, and handle errors efficiently**



