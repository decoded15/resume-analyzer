import streamlit as st
import requests

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your resume PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume uploaded successfully!")
    target_role = st.selectbox(
        "Select Target Role",
        [
            "Data Analyst",
            "Backend Developer",
            "AI Engineer",
            "Software Engineer",
            "Business Analyst"
        ]
    )
    if st.button("Analyze Resume"):

        with st.spinner("Analyzing resume..."):

            files = {
                "file": uploaded_file
            }

            response = requests.post(
                "http://127.0.0.1:8000/upload-resume",
                files=files,
                data = {
                    "target_role": target_role
                }
            )
            data = response.json()

        st.success("Resume analyzed successfully!")

        ats_data = data["ats_analysis"]

        st.subheader("Overall ATS Score")

        st.metric(
            label="ATS Score",
            value=f"{ats_data['overall_score']}/100"
        )

        st.subheader("Score Breakdown")

        breakdown = ats_data["score_breakdown"]

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Formatting", breakdown["formatting"])
            st.metric("Skills", breakdown["skills"])
            st.metric("Impact", breakdown["impact"])

        with col2:
            st.metric("Keyword Optimization", breakdown["keyword_optimization"])
            st.metric("Readability", breakdown["readability"])

        role_data = data["role_fit_analysis"]

        st.subheader("Role Fit Analysis")

        st.metric(
            "Role Fit Score",
            f"{role_data['role_fit_score']}/100"
        )

        st.subheader("Role Fit Summary")

        st.write(role_data["role_fit_summary"])

        st.subheader("Matching Skills")

        for skill in role_data["matching_skills"]:
            st.success(skill)

        st.subheader("Missing Skills")

        for skill in role_data["missing_skills"]:
            st.error(skill)

        st.subheader("Improvement Recommendations")

        for rec in role_data["improvement_recommendations"]:
            st.info(rec)

        st.subheader("Strengths")

        for strength in ats_data["strengths"]:
            st.success(strength)

        st.subheader("Weaknesses")

        for weakness in ats_data["weaknesses"]:
            st.error(weakness)

        st.subheader("Improvement Suggestions")

        for suggestion in ats_data["improvement_suggestions"]:
            st.info(suggestion)