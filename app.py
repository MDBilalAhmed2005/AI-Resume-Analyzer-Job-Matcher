import streamlit as st
import pandas as pd
from resume_parser import extract_text_from_pdf
from skills import extract_skills
from ranking import rank_resumes

st.title("🤖 AI Resume Analyzer & Job Matcher")

st.markdown(
    "### Intelligent resume screening powered by NLP and Machine Learning"
)

st.write(
    "Upload multiple resumes, compare them with a job description, "
    "analyze candidate skills, and generate an HR-ready ranking report."
)



uploaded_files = st.file_uploader(
    "Upload resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True,
    key="resume_uploader"
)


job_description = st.text_area(
    "Enter the Job Description",
    height=200,
    placeholder="Example: Python developer with experience in Pandas, Scikit-learn, Machine Learning and SQL."
)


if uploaded_files:

    resumes = []

    for uploaded_file in uploaded_files:

        text = extract_text_from_pdf(uploaded_file)

        resumes.append(
            (uploaded_file.name, text)
        )

    st.success(
        f"{len(resumes)} resume(s) uploaded successfully!"
    )


    if job_description.strip():

        results = rank_resumes(
            resumes,
            job_description
        )
        st.subheader("Candidate Overview")

        total_candidates = len(results)
        top_score = max(result["Score"] for result in results)
        average_score = sum(result["Score"] for result in results) / total_candidates

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Resumes Analyzed", total_candidates)

        with col2:
            st.metric("Top Match Score", f"{top_score}%")

        with col3:
            st.metric("Average Match Score", f"{average_score:.2f}%")
        st.subheader("Resume Ranking")

        ranking_data = []

        for result in results:

            rank = result["Rank"]
            candidate = result["Candidate"]
            score = result["Score"]

            if score >= 60:
                status = "Strong Match"
            elif score >= 45:
                status = "Good Match"
            else:
                status = "Needs Review"

            ranking_data.append({
                "Rank": rank,
                "Candidate": candidate,
                "Match Score": f"{score}%",
                "Status": status
            })

        st.table(ranking_data)
        report_df = pd.DataFrame(ranking_data)

        csv = report_df.to_csv(index=False)

        st.download_button(
            label="Download HR Report",
            data=csv,
            file_name="resume_ranking_report.csv",
            mime="text/csv"
        )
    


        st.subheader("Skill Analysis")

        job_skills = extract_skills(job_description)

        for result in results:

            candidate = result["Candidate"]
            score = result["Score"]

            resume_text = ""

            for resume_name, text in resumes:
                if resume_name == candidate:
                    resume_text = text
                    break

            resume_skills = extract_skills(resume_text)

            matched_skills = [
                skill for skill in job_skills
                if skill in resume_skills
            ]

            missing_skills = [
                skill for skill in job_skills
                if skill not in resume_skills
            ]

            st.markdown(f"### {candidate}")

            st.write(f"**Match Score:** {score}%")

            st.write(
                "**Matched Skills:** "
                + (", ".join(matched_skills) if matched_skills else "None")
            )

            st.write(
                "**Missing Skills:** "
                + (", ".join(missing_skills) if missing_skills else "None")
            )