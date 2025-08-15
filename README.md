# 📄 ATS Resume Analyzer

An interactive **Streamlit** web app that analyzes resumes against job descriptions and calculates an **ATS (Applicant Tracking System) Score**.  
This tool helps job seekers **optimize their resumes** by identifying missing keywords and improving their chances of passing ATS filters.

---

## 🚀 Features
- 📂 Upload your **resume** (PDF/DOCX)
- 📝 Paste the **job description**
- 📊 Get an **ATS Score** based on keyword matching
- 📌 See **Matched** and **Missing** keywords
- ⚠ Receive improvement suggestions
- 🎯 Simple & user-friendly **Streamlit UI**

---

## 🛠 Tech Stack

| Tool / Library | Purpose |
|----------------|---------|
| **Python**     | Core backend logic |
| **Streamlit**  | Interactive web app framework |
| **docx2txt**   | Extract text from DOCX files |
| **PyPDF2**     | Extract text from PDF files |
| **Regex**      | Keyword extraction and matching |

---

## installation:
* step_1:
    - description: Clone the repository
    - command: git clone https://github.com/yourusername/ats-resume-analyzer.git
* step_2:
    - description: Navigate to the project folder
    - command: cd ats-resume-analyzer
* step_3:
    - description: Install dependencies
    - command: pip install -r requirements.txt
* step_4:
    - description: Run the application
    - command: streamlit run app.py
 
---

# 💡 Future Improvements
* AI-based semantic keyword matching (detects related skills)

* Highlight missing keywords inside resume text

* Export analysis report as PDF

