## 📄 **Context Management**

* **English:** Managing and tracking information during a system or application's operation so it remembers what happened before.
* **Urdu:** System ya application ke chalne ke dauran maloomat ko track aur manage karna taake pehle kya hua tha, wo yaad rahe.


### **2. Why We Use It**

* 🔹 **Consistency** — Maintains the same state
* 🔹 **Accuracy** — Produces relevant results
* 🔹 **Efficiency** — Reduces repeated work
* 🔹 **State Tracking** — Keeps track of the current step


### **3. Types of Context Management**

#### **1️⃣ Local Context**

* Remembers data only in the **current session**
* Storage: Local memory, variables, temporary files
* Scope: Valid until the program is running
* Example: `let userName = "Sumbal"` — deleted after the program ends

#### **2️⃣ LLM Context**

* Large Language Model’s own **conversation history memory**
* Storage: Inside the model (history/embeddings)
* Scope: Valid during conversation or until explicitly saved
* Example: Remembering your previous question in chat


### **4. Local vs LLM Context**

| Feature         | Local Context 🖥           | LLM Context 🧠                |
| --------------- | -------------------------- | ----------------------------- |
| **Storage**     | Local machine memory       | Model memory/history          |
| **Scope**       | Until program/session ends | Until conversation/model ends |
| **Persistence** | Deleted when program ends  | Stays until cleared           |
| **Access**      | Direct through code        | Through prompts               |
| **Example**     | Variables, temp files      | Previous chat turns           |


### **5. Summary**

* Context Management = Maintaining the flow of information
* **Local** → Short-term, program-specific
* **LLM** → Model-specific, remembers conversation history
