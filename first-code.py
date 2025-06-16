from openai import OpenAI

client = OpenAI(api_key="Add your OpenAI API key here")

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(response.choices[0].message.content)