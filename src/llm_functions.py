from openai import OpenAI

def finance_chatbot(messages, model):
  # Replace with your desired model
  client = OpenAI()

  response = client.chat.completions.create(
      model=model,
      messages=messages,
      n=1,
      stop=None,
  )

  response = response.choices[0].message.content

  return response


def table_cleaner(data):
  # Replace with your desired model
  client = OpenAI()
  model_engine = "gpt-4o-mini"

  prompt = f"""Take this data: {data}
    and make it more compact WITHOUT removing any data. Just try to make it a string of less characters"""

  messages = [
    {"role": "system",
     "content": "You are an expert in taking tables in string format with junk text and producing a cleaner version of the table in the same format but more compact and easily readable"},
    {"role": "user",
     "content": prompt}
    ]
    

  response = client.chat.completions.create(
      model=model_engine,
      messages=messages,
      max_tokens=2000,
      n=1,
      stop=None,
      temperature=0.7
  )

  response = response.choices[0].message.content

  return response
