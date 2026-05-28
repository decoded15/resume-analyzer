import streamlit as st
import requests

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your resume PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing resume..."):

            files = {
                "file": uploaded_file
            }

            response = requests.post(
                "http://127.0.0.1:8000/upload-resume",
                files=files
            )

            data = response.json()

        st.success("Resume analyzed successfully!")

        ats_data = data["ats_analysis"]

        st.subheader("ATS Score")

        st.metric(
            label="ATS Score",
            value=f"{ats_data['ats_score']}/100"
        )

        st.subheader("Strengths")

        for strength in ats_data["strengths"]:
            st.success(strength)

        st.subheader("Weaknesses")

        for weakness in ats_data["weaknesses"]:
            st.error(weakness)

        st.subheader("Improvement Suggestions")

        for suggestion in ats_data["improvement_suggestions"]:
            st.info(suggestion)