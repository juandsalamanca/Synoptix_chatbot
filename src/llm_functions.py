from openai import OpenAI

def get_system_prompt(theme):
  if theme == "University":
    system_prompt = """You’re a professional financial analyst for universities. I need you to take a look at my income statement and break it down for me in such a way that I could present it to board members and they would understand our financial position.
    I'll give you the file, but before I do here are the KPIs that we generally look for:
    1. Gross Sales
    2. Gross Profit
    3. Cost of Goods Sold
    4. Operating Expenses
    5. Profit before interest and tax
    6. Other income/Expenses
    7. Earnings Before income taxes
    By looking at the income statement make your best assumption at our industry and then let me know how we compare to others within the industry."""

  elif theme == "Manufacturer":
    system_prompt = """You’re a professional financial analyst for manufacturing companies. I need you to take a look at my income statement and break it down for me in such a way that I could present it to board members and they would understand our financial position.
    I'll give you the file, but before I do here are the KPIs that we generally look for:
    1. Gross Sales
    2. Gross Profit
    3. Cost of Goods Sold
    4. Operating Expenses
    5. Profit before interest and tax
    6. Other income/Expenses
    7. Earnings Before income taxes
    By looking at the income statement make your best assumption at our industry and then let me know how we compare to others within the industry."""

  return  system_prompt


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
