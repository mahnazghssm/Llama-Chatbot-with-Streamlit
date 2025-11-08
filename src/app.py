import streamlit as st

from utils import call_llama

# Title and description of the Streamlit chatbot app
st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Llama :llama:")

# Initialize the chat messages in session state if not already present
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I assist you?"}
    ]

# Display the chat messages in the app
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Capture user input from chat input box
if prompt := st.chat_input():
    # Add the user's message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user's message immediately
    st.chat_message("user").write(prompt)
    
    # Show a spinner while the response is being generated
    with st.spinner("Generating response..."):
        # Call the Llama model to generate a response
        response_msg = call_llama("llama2", prompt)["response"]
    
    # Add the assistant's response to session state
    st.session_state.messages.append({"role": "assistant", "content": response_msg})
    
    # Display the assistant's response
    st.chat_message("assistant").write(response_msg)
