import streamlit as st
import docx2txt
import PyPDF2
import re

# ------------------------------
# Helper: Extract text from PDF
# ------------------------------
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# ------------------------------
# Helper: Extract text from DOCX
# ------------------------------
def extract_text_from_docx(file):
    return docx2txt.process(file)

# ------------------------------
# Helper: Calculate ATS score
# ------------------------------
def calculate_ats_score(resume_text, jd_text):
    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    # Extract keywords from JD
    jd_keywords = set(re.findall(r'\b[a-zA-Z]+\b', jd_text))
    resume_keywords = set(re.findall(r'\b[a-zA-Z]+\b', resume_text))

    # Match percentage
    matched_keywords = jd_keywords.intersection(resume_keywords)
    score = round((len(matched_keywords) / len(jd_keywords)) * 100, 2)

    return score, matched_keywords, jd_keywords - matched_keywords

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="ATS Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 ATS Resume Analyzer")
st.write("Upload your resume and job description to check ATS score.")

# File uploaders
resume_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("Paste the Job Description here")

if resume_file and jd_text.strip():
    # Extract resume text
    if resume_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(resume_file)
    elif resume_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_text_from_docx(resume_file)
    else:
        st.error("Unsupported file type")
        st.stop()

    # Calculate score
    score, matched, missing = calculate_ats_score(resume_text, jd_text)

    st.subheader(f"✅ ATS Score: {score}%")
    st.progress(score / 100)

    st.write("**Matched Keywords:**", ", ".join(matched))
    st.write("**Missing Keywords:**", ", ".join(missing))

    if score < 60:
        st.warning("⚠️ Your resume might not pass ATS filters. Try adding more missing keywords naturally.")
    else:
        st.success("🎉 Your resume is well-aligned with the job description!")

