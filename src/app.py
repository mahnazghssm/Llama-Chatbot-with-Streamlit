import streamlit as st

from utils import call_llama

# Title of the Streamlit application
st.title("💬 Chatbot")
st.caption("🚀 A Streamlit cxhatbot powered by Llama :llama: ")

# Initialize session state for messages if it doesn't exist
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I assist you?"}]  # Default assistant message

# Display chat messages stored in session state
for msg in st.session_state.messages:
    # Display each message according to its role (user or assistant)
    st.chat_message(msg["role"]).write(msg["content"])

# Capture user input from the chat input box
if prompt := st.chat_input():
    # Add the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display the user's message in the chat
    st.chat_message("user").write(prompt)
    
    # Indicate that a response is being generated
    with st.spinner("Generating response..."):
        # Call the Llama model to get a response based on the user's prompt
        msg = call_llama("llama2", prompt)["response"]  # Assuming call_llama returns a dict with a "response" key
    
    # Add the assistant's response to the session state
    st.session_state.messages.append({"role": "assistant", "content": msg})
    
    # Display the assistant's message in the chat
    st.chat_message("assistant").write(msg)