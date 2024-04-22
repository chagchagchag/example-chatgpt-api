from openai import OpenAI
import os

key = os.getenv("OPEN_AI_KEY")
client = OpenAI(api_key = key)

prompt = """
마지막 문장이 긍정적이라면 '긍정적인 기사에요' 를, 부정적이라면 '부정적인 기사에요' 를 표시해주세요.

query: 삼성중공업, 드디어 흑자전환
sentiment: 긍정적인 기사에요

query: 조선업, 달러 강세시 실적에는 조금 부정적인 영향
sentiment: 부정적인 기사에요

query:  
"""

question = input("질문을 입력해주세요 >> ")

prompt = prompt + question + "\nsentiment: "

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  max_tokens=7,
  temperature=0
)

# print(f"response = {response}")
print(response.choices[0].text)