import streamlit as st
from preprocess_fiel import pre_process_file
from src.llm_functions import finance_chatbot, get_system_prompt
st.header("Synoptics")

reset = st.button("Reset")
if reset:
  st.session_state.memory = []
  model = None
  theme = None
  input = None
  response = None

if "memory" not in st.session_state:
  st.session_state.memory = []

model = st.selectbox(("Please choose the model to analyze and discuss the documents"), ("gpt-4o", "gpt-4o-mini", "o1"))

theme = st.selectbox(("Please select the type entity to which the documents belong to"), ("University", "Manufacturer"))

file = st.file_uploader("Upload your file")
if file:
  st.write(file)

pre_processed_data = pre_process_file(file)

if theme and len(st.session_state.memory) == 0:
  sys_prompt = get_system_prompt(theme, data)
  st.session_state.memory.append({"role": "system", "content": sys_prompt})


if theme and model:
  
  input = st.chat_input(
      "Ask something...", 
      key="user_input"
  )
  
  if input:
    st.session_state.memory.append({"role": "user", "content": input})
    response = finance_chatbot(st.session_state.memory)
    st.session_state.memory.append({"role": "assistant", "content": response})
    
  for i, message in enumerate(st.session_state.memory[1:]):
      with st.chat_message(message["role"]):
          content = message["content"]
          if message["role"] != "system":
            st.markdown(content)
