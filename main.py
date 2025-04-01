import streamlit as st
import os
from src.pre_process_files import pre_process_file
from src.llm_functions import finance_chatbot, get_system_prompt

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
 
st.header("Synoptics")

reset = st.button("Reset")
if reset:
  st.session_state.memory = [{"role": "system", "content": None}]
  model = None
  theme = None
  input = None
  response = None

if "memory" not in st.session_state:
  st.session_state.memory = [{"role": "system", "content": None}]

model = st.selectbox(("Please choose the model to analyze and discuss the documents"), ("gpt-4o-mini", "gpt-4o", "o1"))

theme = st.selectbox(("Please select the type entity to which the documents belong to"), ("University", "Manufacturer"))

@st.cache_data
def get_data(file):
  data = pre_process_file(file)
  return data

pre_processed_data = None
file = st.file_uploader("Upload your file")
if file:
  st.write(file.name)
  pre_processed_data = get_data(file)

sys_prompt = get_system_prompt(theme, pre_processed_data)
if st.session_state.memory[0]["content"] != sys_prompt:
  st.session_state.memory.append({"role": "system", "content": sys_prompt})


if theme and model:
  
  input = st.chat_input(
      "Ask something...", 
      key="user_input"
  )
  
  if input:
    st.session_state.memory.append({"role": "user", "content": input})
    response = finance_chatbot(st.session_state.memory, model)
    st.session_state.memory.append({"role": "assistant", "content": response})

  message_list = st.session_state.memory[1:]
  if message_list:
   st.write("We're in")
  	for i, message in enumerate(message_list):
     with st.chat_message(message["role"]):
         content = message["content"]
         if message["role"] != "system":
           st.markdown(content)
