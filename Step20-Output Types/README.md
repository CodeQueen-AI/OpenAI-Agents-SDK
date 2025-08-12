## 📄 **Output Types**


* **English:** The different formats or structures in which an agent can return its response or result.
* **Urdu:** Wo mukhtalif formats ya structures jin me agent apna jawab ya result wapas bhej sakta hai


### **2. Why We Use Them**

* 🔹 **Flexibility** — Choose the best format for the task.
* 🔹 **Compatibility** — Match the output with the system or app requirements.
* 🔹 **Clarity** — Make results easier to read or process.
* 🔹 **Control** — Decide exactly how the response should be structured

  
### **3. Common Output Types**

1. **Text** → Normal plain text output.
2. **JSON** → Structured data in key-value pairs (easy for code to read).
3. **Tool Calls** → Output that triggers another function or tool.
4. **Streaming** → Sends parts of the output in real time instead of all at once.


### **4. Examples**

* **Text:** `"The weather today is sunny."`
* **JSON:** `{"weather": "sunny", "temperature": 30}`
* **Tool Call:** `"Call weatherAPI with location=Karachi"`
* **Streaming:** Sends `"The" → " weather" → " is sunny."` step by step


### **5. Comparison Table**

| Output Type   | Use Case                      | Example                             |
| ------------- | ----------------------------- | ----------------------------------- |
| **Text**      | Human-readable answer         | `"Paris is the capital of France."` |
| **JSON**      | Machine-readable data         | `{"capital": "Paris"}`              |
| **Tool Call** | Trigger an external function  | `"Call translateAPI"`               |
| **Streaming** | Show output as it’s generated | `"The" → " answer" → " is..."`      |


### **6. Summary**

* Output Types = **Different ways for an agent to return its results**.
* Choose based on whether the output is for humans, other programs, or real-time display

