import os
import sys
import logging

from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_TRACING_ENABLED"] = "false"

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

api_key = os.getenv("GroqKey")
model = os.getenv("MODEL", "").strip()

if not api_key or not model:
    raise SystemExit("GroqKey or MODEL not found. Check your .env file.")

if model.startswith("openai/"):
    model = "openai/" + model
else:
    model = "openai/openai/" + model


llm = LLM(
    model="openai/openai/gpt-oss-120b",
    custom_openai=True,
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key,
    temperature=0.2
)

print("CrewAI model:", llm.model)

logging.getLogger("crewai.llms.base_llm").setLevel(logging.ERROR)