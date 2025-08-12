import streamlit as st
import requests

st.title("ConsciousDay Agent")

with st.form("daily_form"):
    journal = st.text_area("Morning Journal")
    dream = st.text_area("Dream")
    intention = st.text_input("Intention of the Day")
    priorities = st.text_area("Top 3 Priorities")
    submitted = st.form_submit_button("Submit")

if submitted:
    res = requests.post(
        "http://localhost:5000/process",
        json={
            "journal": journal,
            "dream": dream,
            "intention": intention,
            "priorities": priorities
        }
    )
    if res.status_code == 200:
        data = res.json()
        st.subheader("Inner Reflection Summary")
        st.write(data["reflection"])
        st.subheader("Dream Interpretation")
        st.write(data["dreamInterpretation"])
        st.subheader("Mindset Insight")
        st.write(data["mindsetInsight"])
        st.subheader("Optimized Day Strategy")
        st.write(data["strategy"])
