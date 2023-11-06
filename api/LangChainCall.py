# install langchaing, open api, create the key
# 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

import os
# from dotenv import load_dotenv
import openai
import langchain

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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";

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with statements, and your task is to convert them to standard English."
    },
    {
      "role": "user",
      "content": "She no went to the market."
    },
    {
      "role": "assistant",
      "content": "test ths"
    }
  ],
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)