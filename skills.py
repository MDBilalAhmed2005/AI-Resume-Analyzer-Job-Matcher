import re


SKILLS = [
    "Python",
    "Java",
    "C++",
    "C",
    "SQL",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Data Analysis",
    "Matplotlib",
    "Seaborn",
    "TensorFlow",
    "Keras",
    "PyTorch",
    "NLP",
    "SpaCy",
    "Flask",
    "Streamlit",
    "GitHub",
    "Git",
    "Excel",
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills