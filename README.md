![oreilly-logo](images/oreilly.png)

# Designing and Deploying LLM Pipelines

This repository contains code for the [O'Reilly Live Online Training for Designing and Deploying LLM Pipelines](https://learning.oreilly.com/live-events/designing-and-deploying-llm-pipelines/0642572014796)

In this comprehensive course, machine learning engineers and software developers learn how to transition large language model (LLM) prototypes into fully deployed production systems. Through detailed instruction and real-world case studies, you explore the best practices for integrating LLMs into diverse workflows, ensuring that your models perform effectively in practical applications.

## Setup Instructions

### Using Python 3.11 Virtual Environment

At the time of writing, we need a Python virtual environment with Python 3.11.

#### Option 1: Python 3.11 is Already Installed

##### Step 1: Verify Python 3.11 Installation

```bash
python3.11 --version
```

##### Step 2: Create a Virtual Environment

```bash
python3.11 -m venv .venv
```

This creates a `.venv` folder in your current directory.

##### Step 3: Activate the Virtual Environment

- **macOS/Linux:**
  
  ```bash
  source .venv/bin/activate
  ```

- **Windows:**
  
  ```cmd
  .venv\Scripts\activate
  ```

You should see `(.venv)` in your terminal prompt.

##### Step 4: Verify the Python Version

```bash
python --version
```

##### Step 5: Install Packages

```bash
pip install -r requirements.txt
```

##### Step 6: Deactivate the Virtual Environment

```bash
deactivate
```

---

#### Option 2: Install Python 3.11

If you don’t have Python 3.11, follow the steps below for your OS.

##### **macOS (Using Homebrew)**

```bash
brew install python@3.11
```

##### **Ubuntu/Debian**

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv
```

##### **Windows (Using Windows Installer)**

1. Go to [Python Downloads](https://www.python.org/downloads/release/python-3110/).
2. Download the installer for Python 3.11.
3. Run the installer and ensure **"Add Python 3.11 to PATH"** is checked.

### Verify Installation

```bash
python3.11 --version
```

You might need to run this command to make the venv findable in jupyter

```bash
python -m ipykernel install --user --name=oreilly-ai-pipelines --display-name "Python (oreilly-ai-pipelines)"
```


## Notebooks

- [Using Evaluation to combat AI drift](https://colab.research.google.com/drive/14E6DMP_RGctUPqjI6VMa8EFlggXR7fat?usp=sharing)


- [Model Training/Serving with BERT](notebooks/model_serving.ipynb)

- [Deploying models with FastAPI](deploy/)

- [Third party model inference](notebooks/third_party_inference.ipynb)


- **Agents**

	- [Introduction to LangGraph](notebooks/LangGraph_Hello_World.ipynb)
	- [Introduction to CrewAI](notebooks/CrewAI_Hello_World.ipynb)
	- [CrewAI Streamlit Demo](notebooks/crewai_streamlit/)

## Instructor

**Sinan Ozdemir** is the Founder and CTO of LoopGenius where he uses State of the art AI to help people run digital ads on Meta, Google, and more. Sinan is a former lecturer of Data Science at Johns Hopkins University and the author of multiple textbooks on data science and machine learning. Additionally, he is the founder of the recently acquired Kylie.ai, an enterprise-grade conversational AI platform with RPA capabilities. He holds a master’s degree in Pure Mathematics from Johns Hopkins University and is based in San Francisco, CA.