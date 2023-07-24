import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Act as a person with good sense of humor who replies everytime in a funny way"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "A Funny Guy")

demo.launch(share = True)
