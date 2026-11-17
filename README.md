# AI-Powered Python Code Review and Bug Detection System

A Python project demonstrating how **CrewAI** can be used to analyze Python code through specialized AI agents. It explores different ways to organize agents, execute tasks, use custom tools, and generate structured code review results.

## Project Overview

The project uses the Groq API with the `openai/gpt-oss-120b` model. Different CrewAI workflows are implemented to analyze Python code, detect potential bugs, identify selected risky patterns, and suggest code improvements.

Rather than being one large application, the project is organized into six independent Python scripts. Each script demonstrates a different CrewAI concept.

## Project Structure

```text
AI-Code-Review-System/
│
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── 01_first_crew.py
├── 02_agent_personalities.py
├── 03_sequential_review.py
├── 04_code_analysis_tools.py
├── 05_structured_review.py
└── 06_hierarchical_review.py
```

## CrewAI Implementations

| File | Implementation |
|---|---|
| `01_first_crew.py` | Basic agent, task, and crew |
| `02_agent_personalities.py` | Multiple agents with different roles, goals, and backstories |
| `03_sequential_review.py` | Sequential task execution with context |
| `04_code_analysis_tools.py` | Custom tools using the `@tool` decorator |
| `05_structured_review.py` | Structured review output using Pydantic |
| `06_hierarchical_review.py` | Hierarchical process with a manager LLM |

## Technologies

- Python
- CrewAI
- Groq API
- OpenAI GPT-OSS 120B
- Pydantic
- python-dotenv

## Getting Started

**1. Clone the repository**

```bash
git clone <repository-url>
cd AI-Code-Review-System
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure your API key**

Create a `.env` file in the project directory:

```dotenv
GroqKey=your_groq_api_key
MODEL=openai/gpt-oss-120b
```

Replace `your_groq_api_key` with your Groq API key.

**5. Run a script**

Run any of the six implementations individually:

```bash
python 01_first_crew.py
```

For example, to run the structured review:

```bash
python 05_structured_review.py
```

## Example

The scripts use sample Python code for analysis, including a function that calculates the average of a list of numbers. The agents can explain its functionality, identify potential issues such as division by zero, and recommend improvements.

## Notes

- Each script demonstrates a separate CrewAI implementation.
- The project requires an active Groq API key and an internet connection.
- AI-generated code reviews should be checked manually.
- The custom pattern detection tool checks selected patterns and is not a complete security scanner.
- Keep `.env` private and do not commit API keys to the repository.

## Purpose

Developed as an academic project to practice and demonstrate the core concepts of CrewAI through a Python code review and bug detection use case.
