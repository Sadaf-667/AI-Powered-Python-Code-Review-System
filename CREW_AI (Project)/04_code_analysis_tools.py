from config import llm
from crewai import Agent, Task, Crew
from crewai.tools import tool


@tool("Count Code Lines")
def count_code_lines(code: str) -> str:
    """Count total, non-empty, and blank lines in Python code."""
    lines = code.splitlines()
    total = len(lines)
    non_empty = sum(1 for line in lines if line.strip())
    blank = total - non_empty

    return (
        f"Total lines: {total}\n"
        f"Non-empty lines: {non_empty}\n"
        f"Blank lines: {blank}"
    )


@tool("Find Risky Python Patterns")
def find_risky_patterns(code: str) -> str:
    """Find potentially risky patterns in Python source code."""
    patterns = {
        "eval(": "Dynamic code execution",
        "exec(": "Dynamic code execution",
        "except:": "Bare exception handling",
        "while True:": "Potential infinite loop",
        "input(": "User input requiring validation"
    }

    findings = []

    for pattern, description in patterns.items():
        if pattern in code:
            findings.append(f"{pattern} - {description}")

    if not findings:
        return "No common risky patterns detected."

    return "\n".join(findings)


code_analyzer = Agent(
    role="Python Code Analysis Specialist",
    goal="Analyze Python code using custom tools and explain possible issues.",
    backstory="You are skilled at inspecting Python code and using analysis tools to identify potential problems.",
    llm=llm,
    tools=[count_code_lines, find_risky_patterns],
    verbose=True
)

analysis_task = Task(
    description=(
        "Analyze the following Python code:\n\n"
        "{code}\n\n"
        "Use both available tools to inspect the code. "
        "Report the line statistics, detected risky patterns, "
        "and explain the overall purpose of the code. "
        "Do not claim that a pattern is definitely a bug without evidence."
    ),
    expected_output=(
        "A code analysis report containing line statistics, "
        "risky patterns, and an explanation of the code."
    ),
    agent=code_analyzer
)

crew = Crew(
    agents=[code_analyzer],
    tasks=[analysis_task],
    verbose=True
)

result = crew.kickoff(
    inputs={
        "code": """
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

marks = [80, 90, 75, 85]
print(calculate_average(marks))
"""
    }
)

print("\n===== CUSTOM TOOL ANALYSIS REPORT =====")
print(result.raw)
