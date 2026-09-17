import streamlit as st

from utils import call_llama

st.title("Chatbot")
st.caption("A Streamlit chatbot powered by Llama")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I assist you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    st.chat_message("user").write(prompt)

    with st.spinner("Generating response..."):
        result = call_llama("llama2", prompt)

    if isinstance(result, dict):
        msg = result["response"]
        st.session_state.messages.append(
            {"role": "assistant", "content": msg}
        )
        st.chat_message("assistant").write(msg)
    else:
        st.chat_message("assistant").write(result)
