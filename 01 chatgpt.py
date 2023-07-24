import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)