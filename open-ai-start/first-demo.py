from openai import OpenAI
import os

key = os.getenv("OPEN_AI_KEY")
client = OpenAI(api_key = key)

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)
print(f"response = {response}")