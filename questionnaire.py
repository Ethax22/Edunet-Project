# questionnaire.py
import streamlit as st

def get_user_input():
    st.title("Entrepreneur Guidance - Start Here")
    stage = st.selectbox("Which stage are you at?", ["Idea", "MVP", "Product-Market Fit", "Scaling", "Fundraising"])
    challenge = st.text_area("Describe your current biggest challenge:")
    goal = st.text_input("What is your short-term goal?")
    return stage, challenge, goal
