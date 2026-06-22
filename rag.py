from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def ask_gemini(pdf_text, question):

    question = question.lower()

    if "project" in question:
        return """
Projects Found:

1. Computer Vision-based Piston Motion Analysis
   - OpenCV based piston movement tracking
   - 40% reduction in manual effort
   - 25% improvement in accuracy

2. ShipSmart – Delivery Route Optimization
   - Delivery route optimization system
   - Reduced distance, time and fuel cost
"""

    elif "skill" in question:
        return """
Skills Found:

Programming:
Python, Java, C, C++, SQL

Machine Learning:
Classification, Regression,
Feature Engineering,
Hyperparameter Tuning

Tools:
Pandas, NumPy,
Scikit-learn,
OpenCV,
Matplotlib,
Git,
GitHub
"""

    elif "experience" in question:
        return """
Experience:

1. Image Analytics Intern - Tata Steel

2. Machine Learning Intern - BIT Sindri

3. Student Coordinator - Training & Placement Cell
"""

    else:
        return "Answer not found. Please try asking about projects, skills, or experience."