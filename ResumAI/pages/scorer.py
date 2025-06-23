import streamlit as st
import PyPDF2
import io
import os
import requests
import re
from dotenv import load_dotenv
from streamlit_extras.switch_page_button import switch_page

load_dotenv()

st.set_page_config(page_title="ResumAI", page_icon="📝", layout="wide")


st.markdown("""
    <style>
        /* Completely hide the sidebar */
        [data-testid="stSidebar"] {
            display: none !important;
        }

        /* Hide the hamburger (sidebar toggle) button */
        [data-testid="collapsedControl"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

if st.button("🔙 Back to Home"):
    st.switch_page("app.py")



st.markdown("""
    <style>
            
    .stApp {
        background-color: #bf7b5a;
        color: #2e2d2b
    }
            
    .stFileUploader label {
        color: #2e2d2b;
        font-weight: bold;
    }

    .stTextInput > label {
        color: #2e2d2b;
        font-weight: bold;
    }
            
    div.stButton > button {
        background-color: #f28f16;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
        border: none;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: #e5780f;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)



st.title("ResumAI Scorer📝")
st.markdown("Upload your resume and get **AI-powered score** based on your resume")

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    st.error("❌ OPENROUTER_API_KEY not found. Add it to your .env file.")
    st.stop()

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targeting (optional)")
analyzeBtn = st.button("Analyze your Resume")

def parse_PDF(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_Text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return parse_PDF(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyzeBtn and uploaded_file:
    try:
        file_content = extract_Text(uploaded_file)

        if not file_content.strip():
            st.error("❌ The uploaded file is empty or unreadable.")
            st.stop()

        prompt = f"""You are an expert resume evaluator. Carefully review the resume below and assign a total score out of 100. 

Break the score into **exactly four categories**, each out of 25 points:
1. Relevance (to job role)
2. Keywords (usage of industry/job-specific keywords)
3. Clarity (readability, grammar, concise language)
4. Formatting (layout, sectioning, visual structure)

Then compute the **total score out of 100** by summing the above.

Target Role: {job_role if job_role else "General"}

RESUME CONTENT:
{file_content}

⚠️ Return your response **exactly in the following markdown format,This is very serious**:

-Resume Score: XX / 100

**Breakdown**:
- Relevance: X/25 — short explanation
- Keywords: X/25 — short explanation
- Clarity: X/25 — short explanation
- Formatting: X/25 — short explanation

**Final Remarks**: 1–2 lines summarizing strengths and areas of improvement.


⚠️ Do not include extra sections, code, or commentary.
Keep it under 1000 words.
"""


        with st.spinner("⏳ Analyzing your resume..."):
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "deepseek/deepseek-r1-0528:free",
                "messages": [
                    {"role": "system", "content": "You are an expert resume reviewer."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 5000,
                "temperature": 0.7
            }
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

            if response.status_code == 200:
                content = response.json()["choices"][0]["message"]["content"]
                st.success("✅ Analysis complete!")

                # Parse scores
                total = int(re.search(r"Resume Score:\s*(\d+)", content).group(1)) if re.search(r"Resume Score:\s*(\d+)", content) else 0
                relevance = int(re.search(r"Relevance:\s*(\d+)", content).group(1)) if re.search(r"Relevance:\s*(\d+)", content) else 0
                keywords = int(re.search(r"Keywords:\s*(\d+)", content).group(1)) if re.search(r"Keywords:\s*(\d+)", content) else 0
                clarity = int(re.search(r"Clarity:\s*(\d+)", content).group(1)) if re.search(r"Clarity:\s*(\d+)", content) else 0
                formatting = int(re.search(r"Formatting:\s*(\d+)", content).group(1)) if re.search(r"Formatting:\s*(\d+)", content) else 0

                st.metric("🌟 Total Resume Score", f"{total}/100")
                st.progress(total / 100)

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("📌 Relevance", f"{relevance}/25")
                    st.metric("🔑 Keywords", f"{keywords}/25")
                with col2:
                    st.metric("🧐 Clarity", f"{clarity}/25")
                    st.metric("🔠 Formatting", f"{formatting}/25")

                st.markdown("### 💬 AI Feedback Summary")
                st.markdown(f"""
                <div style="background-color:#fff5e6;padding:20px;border-radius:10px;color:#2e2d2b;">
                {content}</div>
                """, unsafe_allow_html=True)

            else:
                st.error(f"❌ API error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")


# --- Footer ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; font-size: 18px; line-height: 2;">
        <p>📞 <strong>Phone:</strong> 0333-0431520</p>
        <p>🔗 <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/uzair-majeed-605611319/" style="color: #ffffff;" target="_blank">linkedin.com/in/uzair-majeed</a></p>
        <p>🐙 <strong>GitHub:</strong> <a href="https://github.com/Uzair-Majeed" style="color: #ffffff;" target="_blank">github.com/Uzair-Majeed</a></p>
        <p>📧 <strong>Email:</strong> <a href="mailto:uzairmjd886@gmail.com" style="color: #ffffff;">uzairmjd886@gmail.com</a></p>
    </div>
""", unsafe_allow_html=True)
