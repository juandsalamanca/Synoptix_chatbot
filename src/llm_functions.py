from openai import OpenAI

def finance_chatbot(messages):
  # Replace with your desired model
  client = OpenAI()
  model_engine = "gpt-o1"

  response = client.chat.completions.create(
      model=model_engine,
      messages=messages,
      max_tokens=500,
      n=1,
      stop=None,
      temperature=0.7
  )

  response = response.choices[0].message.content

  return response
