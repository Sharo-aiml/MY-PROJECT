import streamlit as st
from agents.coordinator import Coordinator

coordinator = Coordinator()

st.title("AI Personal Assistant")

user_input = st.text_input("Enter command")

if st.button("Send"):

    response = coordinator.handle(user_input)

    st.write("Assistant:", response)