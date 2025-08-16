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
        "https://consious-day-agent-be-fbnm.vercel.app/api/generate",
        json={
            "journal": journal,
            "dream": dream,
            "intention": intention,
            "priorities": priorities
        }
    )
    # st.write("Raw response:", res.text)
    if res.status_code == 200:
        data = res.json()
        result = data["result"]

        parts = result.split("\n")
        for line in parts:
            if line.startswith("1."):
                st.subheader("Inner Reflection Summary")
                st.write(line.replace("1. Inner Reflection Summary:", "").strip())
            elif line.startswith("2."):
                st.subheader("Dream Interpretation Summary")
                st.write(line.replace("2. Dream Interpretation Summary:", "").strip())
            elif line.startswith("3."):
                st.subheader("Energy/Mindset Insight")
                st.write(line.replace("3. Energy/Mindset Insight:", "").strip())
            elif line.startswith("4."):
                st.subheader("Suggested Day Strategy")
                st.write(line.replace("4. Suggested Day Strategy (time-aligned tasks):", "").strip())
