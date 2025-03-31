import streamlit as st

st.header("Synoptics")

if "memory" not in st.session_state:
  st.session_state.memory = []

model = st.selectbox(("Please choose the model to analyze and discuss the documents"), ("gpt-4o", "gpt-4o-mini", "o1"))

theme = st.selectbox(("Please select the type entity to which the documents belong to"), ("University", "Manufacturer"))

for i, message in enumerate(st.session_state.memory):
    with st.chat_message(message["role"]):
        content = message["content"]
        if message["role"] == "user":
            idx = content.index("says:")
            content = content[idx+6:]
        st.markdown(content + st.session_state.sensitive_memory[i])
