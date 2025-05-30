import streamlit as st
from sentiment import detect_sentiment
from chatbot import get_bot_response
from voice_input import get_voice_input

st.set_page_config(page_title="Mental Health Support Chatbot", page_icon=":robot_face:", layout="wide")

st.title("Mental Health Support Chatbot 🤖")
st.write("Welcome to the Mental Health Support Chatbot! I'm here to listen and provide support. How are you feeling today?")

user_input = st.text_area("Type your message here:", height=150)

#^ Voice input button
if st.button("🎙️ Speak Instead"):
  with st.spinner("Listening..."):
    voice_text = get_voice_input()
    st.success(f"You said: {voice_text}")
    user_input = voice_text
#^ if there is user input
if user_input:
  sentiment =detect_sentiment(user_input)
  bot_response = get_bot_response(sentiment)
  st.write(f"**Detected Sentiment:** _{sentiment}_")
  st.markdown(f"**Bot Response:** {bot_response}")