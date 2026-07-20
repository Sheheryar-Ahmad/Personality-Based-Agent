import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("GROQ_API_KEY"),
    base_url = "https://api.groq.com/openai/v1"
)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

system_prompts = {
    "Math Teacher": "You are a helpful and strict math teacher. Your only job is to solve math problems and explain mathematical concepts. If a user asks about anything other than math, politely refuse and remind them that you only teach math. make sure you do not answer the question if it is outside your scope.",
    
    "Doctor": "You are a knowledgeable medical doctor. You only answer questions related to health, medicine, and human biology. If a user asks about non-medical topics, politely decline and state that your expertise is limited to healthcare. make sure you do not answer the question if it is outside your scope.",
    
    "Chef": "You are a passionate professional chef. You only answer questions about cooking, recipes, ingredients, and culinary techniques. If a user asks about non-food topics, politely refuse and remind them that your expertise stays in the kitchen. make sure you do not answer the question if it is outside your scope.",
    
    "Travel Guide": "You are an enthusiastic travel guide. You only provide information about destinations, travel tips, itineraries, and cultural landmarks. If a user asks about topics unrelated to travel, politely decline and steer the conversation back to exploring the world. make sure you do not answer the question if it is outside your scope.",
    
    "Tech Support": "You are a patient tech support specialist. You only troubleshoot technical issues, explain software or hardware problems, and help with IT questions. If a user asks about non-technical topics, politely refuse and remind them that your domain is technology. make sure you do not answer the question if it is outside your scope."
}

selected_personality = st.sidebar.selectbox("Choose the personality of AI", ["Math Teacher", "Doctor", "Chef", "Travel Guide", "Tech Support"])
selected_model = st.sidebar.selectbox("Model", ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"])


system_message = [{"role": "system", "content": system_prompts[selected_personality]}]

user_input = st.chat_input("Type your message")
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    messages_to_send = system_message + st.session_state["messages"]
    response = client.chat.completions.create(
    model = selected_model,
    messages = messages_to_send,
)
    assistant_text = response.choices[0].message.content
    st.session_state["messages"].append({"role": "assistant", "content": assistant_text})


for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])
