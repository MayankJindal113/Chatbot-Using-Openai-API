import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a doctor"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Doctor")

demo.launch(share = True)