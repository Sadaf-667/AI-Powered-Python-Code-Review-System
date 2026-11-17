from config import llm
from crewai import Agent, Task, Crew, Process

code_analyzer = Agent(
    role="Python Code Analyzer",
    goal="Analyze the structure and purpose of Python code.",
    backstory="You are an expert at understanding Python programs and explaining their functionality.",
    llm=llm,
    verbose=True
)

bug_detector = Agent(
    role="Python Bug Detector",
    goal="Find logical errors and potential runtime problems.",
    backstory="You are a Python debugging specialist who identifies genuine coding issues.",
    llm=llm,
    verbose=True
)

code_optimizer = Agent(
    role="Python Code Optimizer",
    goal="Suggest practical improvements to Python code.",
    backstory="You specialize in improving Python code readability, efficiency, and maintainability.",
    llm=llm,
    verbose=True
)

analysis_task = Task(
    description=(
        "Analyze the purpose and structure of this Python code:\n\n"
        "{code}"
    ),
    expected_output="An explanation of the code's purpose and structure.",
    agent=code_analyzer
)

bug_task = Task(
    description=(
        "Identify actual bugs and potential runtime errors in this code:\n\n"
        "{code}"
    ),
    expected_output="A list of bugs and explanations. State clearly if none are found.",
    agent=bug_detector
)

optimization_task = Task(
    description=(
        "Suggest useful improvements for this Python code:\n\n"
        "{code}"
    ),
    expected_output="Practical code improvement suggestions.",
    agent=code_optimizer
)

crew = Crew(
    agents=[code_analyzer, bug_detector, code_optimizer],
    tasks=[analysis_task, bug_task, optimization_task],
    process=Process.hierarchical,
    manager_llm=llm,
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

print("\n===== HIERARCHICAL CODE REVIEW =====")
print(result.raw)