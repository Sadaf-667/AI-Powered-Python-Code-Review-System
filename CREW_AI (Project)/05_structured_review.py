from config import llm
from crewai import Agent, Task, Crew
from pydantic import BaseModel, Field


class CodeReview(BaseModel):
    code_purpose: str = Field(description="Purpose of the Python code")
    bugs: list[str] = Field(description="Identified bugs or potential issues")
    suggestions: list[str] = Field(description="Recommended improvements")
    overall_quality: str = Field(description="Overall assessment of code quality")


code_reviewer = Agent(
    role="Python Code Reviewer",
    goal="Review Python code and produce an accurate structured review.",
    backstory="You are an experienced Python reviewer who identifies genuine issues and provides practical improvements.",
    llm=llm,
    verbose=True
)

review_task = Task(
    description=(
        "Review the following Python code:\n\n"
        "{code}\n\n"
        "Identify its purpose, actual bugs or potential issues, "
        "and practical improvements. Do not invent problems. "
        "If no bugs are found, state that clearly."
    ),
    expected_output="A structured Python code review.",
    agent=code_reviewer,
    output_pydantic=CodeReview
)

crew = Crew(
    agents=[code_reviewer],
    tasks=[review_task],
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

print("\n===== STRUCTURED CODE REVIEW =====")

if result.pydantic:
    print(result.pydantic.model_dump_json(indent=4))
else:
    print(result.raw)