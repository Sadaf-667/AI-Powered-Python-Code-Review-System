from config import llm
from crewai import Agent, Task, Crew

code_analyzer = Agent(
    role="Python Code Analyzer",
    goal="Analyze Python code and explain its purpose, structure, and potential issues.",
    backstory="You are a Python code analysis specialist. You examine code carefully and explain technical details in clear language.",
    llm=llm,
    verbose=True
)

analysis_task = Task(
    description=(
        "Analyze the following Python code:\n\n"
        "{code}\n\n"
        "Explain what the code does, identify its main components, "
        "and mention any potential coding issues."
    ),
    expected_output=(
        "A clear code analysis containing the program's purpose, "
        "main components, and potential coding issues."
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

print("\n== CODE ANALYSIS REPORT ==")
print(result.raw)