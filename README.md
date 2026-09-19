# 🤖 AI Resume Analyzer & Job Matcher

An AI-powered web application that analyzes multiple resumes against a job description and automatically ranks candidates based on their relevance.

## 📌 Project Overview

The AI Resume Analyzer & Job Matcher helps reduce the manual effort involved in resume screening.

Users can upload multiple PDF resumes and enter a job description. The application extracts text from each resume, compares it with the job description using TF-IDF and cosine similarity, calculates match scores, ranks candidates, and identifies matched and missing skills.

## ✨ Features

- 📄 Upload multiple PDF resumes
- 📝 Enter a custom job description
- 🤖 AI/ML-based resume matching
- 📊 TF-IDF and cosine similarity scoring
- 🏆 Automatic candidate ranking
- 🧠 Matched skills analysis
- ❌ Missing skills identification
- 🏷️ Candidate suitability status
- 📈 Candidate overview with summary metrics
- 📥 Download HR ranking report as CSV
- 🌐 Interactive Streamlit web interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- pypdf
- Regular Expressions (Regex)
- TF-IDF
- Cosine Similarity

## ⚙️ How It Works

```text
Upload PDF Resumes
        ↓
Extract Resume Text
        ↓
Enter Job Description
        ↓
TF-IDF Vectorization
        ↓
Cosine Similarity
        ↓
Calculate Match Scores
        ↓
Rank Candidates
        ↓
Analyze Matched & Missing Skills
        ↓
Generate HR Report
```

## 📂 Project Structure

```text
AI-Resume-Analyzer-Job-Matcher/
│
├── app.py
├── matcher.py
├── ranking.py
├── resume_parser.py
├── skills.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/MDBilalAhmed2005/AI-Resume-Analyzer-Job-Matcher.git
```

### 2. Open the project

```bash
cd AI-Resume-Analyzer-Job-Matcher
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 📊 Sample Results

The application was tested using multiple sample Data Science resumes and a Data Science job description.

The system successfully:

- Extracted text from PDF resumes
- Calculated resume-job match scores
- Ranked candidates automatically
- Identified matched skills
- Identified missing skills
- Generated an HR-ready CSV report

### Example Output

| Rank | Candidate | Match Score | Status |
|---:|---|---:|---|
| 1 | Sample Resume A | 68.59% | Strong Match |
| 2 | Sample Resume C | 55.89% | Good Match |
| 3 | Sample Resume B | 49.91% | Good Match |

> Note: Match scores are calculated using TF-IDF vectorization and cosine similarity between the resume and job description.

## 🎯 Use Cases

- Resume screening
- Internship candidate matching
- Entry-level recruitment
- HR resume analysis
- Job-specific candidate comparison

## 🚀 Future Improvements

- 🔍 Advanced NLP-based resume understanding
- 🧠 Semantic similarity using transformer models
- 🎯 Job-specific skill weighting
- 📑 Support for DOCX resumes
- 📊 Advanced recruiter analytics dashboard
- 👥 Candidate filtering and search
- 🔐 User authentication
- ☁️ Cloud deployment
- 🤖 AI-generated resume feedback
- 📧 Automated candidate communication

## 👨‍💻 Author

**Mohammed Bilal Ahmed**

B.E. Computer Science & Engineering — Data Science

Interested in Artificial Intelligence, Machine Learning, Data Science and AI-powered applications.

**GitHub:** [MDBilalAhmed2005](https://github.com/MDBilalAhmed2005)