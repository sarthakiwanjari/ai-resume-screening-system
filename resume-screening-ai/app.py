import streamlit as st

# Title
st.title("AI-Based Resume Screening System")

# Input fields
resume_input = st.text_area("Paste Resume Here")
jd_input = st.text_area("Paste Job Description Here")

# ---------------- FUNCTIONS ---------------- #

def extract_info(resume_text):
    lines = resume_text.split("\n")
    
    skills = ""
    experience = ""
    tools = ""
    
    for line in lines:
        if "Skills:" in line:
            skills = line.replace("Skills:", "").strip()
        elif "Experience:" in line:
            experience = line.replace("Experience:", "").strip()
        elif "Tools:" in line:
            tools = line.replace("Tools:", "").strip()
    
    return {
        "skills": skills,
        "experience": experience,
        "tools": tools
    }

def calculate_score(resume_data, job_description):
    jd_skills = ["Python", "Machine Learning", "SQL", "Pandas", "NumPy"]
    
    resume_skills = [skill.strip() for skill in resume_data["skills"].split(",")]
    
    match_count = 0
    
    for skill in jd_skills:
        if skill in resume_skills:
            match_count += 1
    
    score = (match_count / len(jd_skills)) * 100
    
    return score, match_count

def generate_explanation(score, match_count):
    if score == 100:
        return "Candidate perfectly matches all required skills."
    elif score >= 70:
        return f"Candidate matches most required skills ({match_count} matched)."
    elif score >= 40:
        return f"Candidate matches some skills ({match_count} matched)."
    else:
        return "Candidate does not match required skills."

# ---------------- MAIN BUTTON ---------------- #

if st.button("Analyze Resume"):
    if resume_input and jd_input:
        data = extract_info(resume_input)
        score, match_count = calculate_score(data, jd_input)
        explanation = generate_explanation(score, match_count)

        st.subheader("Results")
        st.write("Matching Score:", score)
        st.write("Explanation:", explanation)
    else:
        st.warning("Please enter both Resume and Job Description")