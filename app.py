import streamlit as st
import requests
import json
import time

RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"

st.set_page_config(page_title="AI Career Counsellor", page_icon="🤖")

st.title("🤖 AI Virtual Career Counsellor")
st.markdown("I'm here to help you explore potential career paths based on your interests!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_rasa_response(user_message):
    payload = json.dumps({"sender": "streamlit_user", "message": user_message})
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(RASA_API_URL, data=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to Rasa server. Please ensure Rasa server is running in another terminal.")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while communicating with Rasa: {e}")
        return None
    
if prompt := st.chat_input("What are your career interests? (e.g., tech, arts, business, numbers)"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    rasa_responses = get_rasa_response(prompt)

    with st.chat_message("assistant"):
        if rasa_responses:
            print(f"DEBUG: Raw Rasa response: {rasa_responses}")
            for message in rasa_responses:
                bot_message = message.get("text")
                if bot_message:
                    # message_placeholder = st.empty()
                    # full_response = ""
                    # for chunk in bot_message.split():
                    #     full_response = chunk + " "
                    #     time.sleep(0.30)
                    #     message_placeholder.markdown(full_response + "▌")
                    # message_placeholder.markdown(full_response)
                    st.markdown(bot_message)
                    st.session_state.messages.append({"role": "assistant", "content": bot_message})
        else:
            st.markdown("Sorry, I couldn't get a response from the career counsellor at the moment.")
            st.session_state.messages.append({"role": "assistant", "content": "Sorry, I couldn't get a response from the career counsellor at the moment."})