from openai import OpenAI 

client = OpenAI()

prompt = input("enter your input: ")

response = client.chat.completions.create(
    model= "deepseek-ai/deepseek-v3.1",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)

