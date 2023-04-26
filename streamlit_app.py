import streamlit as st
import requests

# Set up API endpoint and headers
endpoint = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer ",
    "Content-Type": "application/json"
}

# Define function to make API request
def generate_chat_response(messages):
    data = {
        "messages": messages
    }
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        assistant_reply = response.json()['choices'][0]['message']['content']
        return assistant_reply
    else:
        st.warning("Failed to generate chat response. Please try again.")
        return None

# Streamlit app
def main():
    st.title("ChatGPT Web Chat")

    # Input form for user messages
    user_message = st.text_input("You:", key="user_message")
    user_messages = []

    # Add user message to data frame
    if st.button("Send"):
        if user_message:
            user_messages.append({"role": "user", "content": user_message})
            st.text("User: " + user_message)

    # Generate assistant reply and display in the chat window
    assistant_reply = generate_chat_response(user_messages)
    if assistant_reply:
        user_messages.append({"role": "assistant", "content": assistant_reply})
        st.text("Assistant: " + assistant_reply)

if __name__ == "__main__":
    main()
