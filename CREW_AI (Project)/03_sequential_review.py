from config import llm
from crewai import Agent, Task, Crew, Process

code_analyzer = Agent(
    role="Python Code Analyzer",
    goal="Explain the purpose and structure of Python code.",
    backstory="You are skilled at understanding Python programs and explaining their functionality.",
    llm=llm,
    verbose=True
)

bug_detector = Agent(
    role="Python Bug Detector",
    goal="Identify bugs and possible runtime errors in Python code.",
    backstory="You are an experienced debugger who carefully examines code for logical and runtime problems.",
    llm=llm,
    verbose=True
)

code_reviewer = Agent(
    role="Python Code Reviewer",
    goal="Prepare a final review using the analysis and bug detection results.",
    backstory="You are a code reviewer who combines technical findings into a clear and useful report.",
    llm=llm,
    verbose=True
)

analysis_task = Task(
    description=(
        "Analyze the following Python code. Explain its purpose, "
        "main components, and working:\n\n{code}"
    ),
    expected_output="An explanation of the code's purpose and structure.",
    agent=code_analyzer
)

bug_task = Task(
    description=(
        "Identify logical errors, runtime errors, and potential bugs "
        "in the provided Python code:\n\n{code}"
    ),
    expected_output="A list of possible bugs with clear explanations.",
    agent=bug_detector
)

review_task = Task(
    description=(
        "Prepare a final code review using the previous analysis "
        "and bug detection results. Include the code's purpose, "
        "identified issues, and recommended improvements."
    ),
    expected_output="A complete code review report with findings and recommendations.",
    agent=code_reviewer,
    context=[analysis_task, bug_task]
)

crew = Crew(
    agents=[code_analyzer, bug_detector, code_reviewer],
    tasks=[analysis_task, bug_task, review_task],
    process=Process.sequential,
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

print("\n===== SEQUENTIAL CODE REVIEW REPORT =====")
print(result.raw)