from config import llm
from crewai import Agent, Task, Crew

code_analyzer = Agent(
    role="Python Code Analyzer",
    goal="Understand the structure and functionality of Python code.",
    backstory="You are skilled at explaining Python programs and identifying their main components.",
    llm=llm,
    verbose=True
)

bug_detector = Agent(
    role="Python Bug Detector",
    goal="Identify logical errors, runtime errors, and potential bugs in Python code.",
    backstory="You are an experienced Python debugger who carefully examines code to find mistakes and weaknesses.",
    llm=llm,
    verbose=True
)

code_optimizer = Agent(
    role="Python Code Optimizer",
    goal="Suggest improvements to make Python code cleaner, faster, and more efficient.",
    backstory="You are a Python optimization specialist who focuses on code quality, readability, and performance.",
    llm=llm,
    verbose=True
)

analysis_task = Task(
    description=(
        "Analyze this Python code and explain its purpose and structure:\n\n"
        "{code}"
    ),
    expected_output="A clear explanation of the code and its main components.",
    agent=code_analyzer
)

bug_task = Task(
    description=(
        "Examine the Python code and identify possible bugs, "
        "runtime errors, and logical problems:\n\n{code}"
    ),
    expected_output="A list of identified bugs with explanations.",
    agent=bug_detector
)

optimization_task = Task(
    description=(
        "Review the Python code and suggest improvements "
        "for readability, efficiency, and code quality:\n\n{code}"
    ),
    expected_output="Practical suggestions for improving the code.",
    agent=code_optimizer
)

crew = Crew(
    agents=[code_analyzer, bug_detector, code_optimizer],
    tasks=[analysis_task, bug_task, optimization_task],
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

print("\n===== AGENT PERSONALITIES REPORT =====")
print(result.raw)
