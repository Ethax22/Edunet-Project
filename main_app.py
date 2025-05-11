
import streamlit as st
from questionnaire import get_user_input
from roadmap import generate_roadmap
from recommendations import get_resources
from nlp_analysis import analyze_challenge

stage_input, challenge, goal = get_user_input()

if st.button("Generate Guidance"):
    detected_stage = analyze_challenge(challenge)
    st.subheader(f"Detected Stage: {detected_stage}")
    
    roadmap = generate_roadmap(detected_stage)
    st.subheader("Recommended Roadmap:")
    for step in roadmap:
        st.write("✅", step)
    
    recs = get_resources(detected_stage)
    st.subheader("Recommended Resources:")
    for item in recs:
        st.write("📘", item)
