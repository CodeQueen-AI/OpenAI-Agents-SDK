
# 🚀 Setup & Gemini Configuration

## 🚀 Step-by-Step Setup Guide


### 1. **Initialize Project with `uv init`**

```bash
uv init
````

🟡 This command creates important project files:

* `pyproject.toml` – defines your project dependencies.
* `.venv/` – prepares for virtual environment setup.

✅ **Why?** It sets up the foundation for managing Python packages and project structure cleanly

### 2. **Create Virtual Environment with `uv venv`**

```bash
uv venv
```

🔵 This creates a local Python environment inside a `.venv` folder

✅ **Why?** It isolates your project dependencies from the global Python environment, so you avoid conflicts


### 3. **Activate the Virtual Environment**

#### On **Windows**

```bash
.venv\Scripts\activate
```

✅ **Why?** Activating ensures all packages install inside the virtual environment, keeping your project clean and portable


### 4. **Install Required Package: `openai-agents`**

```bash
uv pip install openai-agents
```

✅ **Why?** This installs the tools (`Agent`, `Runner`, `AsyncOpenAI`, etc.) needed to work with AI agents and Gemini in Python


### 5. **Configure Gemini**

#### 📄 Step 1: Create a `.env` file

In the root folder, create a `.env` file with the following content:

```
GEMINI_API_KEY=your-api-key-here
```

✅ This safely stores your Gemini API key


#### ⚙️ Step 2: Create a `config.py` file

In the same folder, create a `config.py` file and paste the following code

```python
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, RunConfig, OpenAIChatCompletionsModel

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.0-flash"
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)
```

✅ **Why?** This sets up your Gemini client using environment variables securely and prepares your AI model for use in other Python files


### 6. **Use Gemini Config in Your Main File**

In your `main.py`, import the `config` from `config.py` like this:

```python
from config import config

run_config = config
```

✅ **What does this mean?**

* `from config import config` → This imports the configuration object from your setup file
* `run_config = config` → This assigns it a local name so it’s easier to use and pass around in your code

✅ **Why do this?**

* Keeps your logic (`main.py`) separate from configuration (`config.py`)
* Makes it easy to reuse the same configuration with multiple AI agents or models


## ✅ You're All Set!

You now have:

* 📁 A structured Python project
* 🧪 Virtual environment created with `uv`
* 🔐 Gemini API securely loaded with `.env`
* ⚙️ A reusable Gemini configuration file
* 🧠 A ready-to-go `main.py` using the config
* 🧰 Installed tools (`openai-agents`) to power your AI agents
