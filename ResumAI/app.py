import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="ResumAI", page_icon="📝", layout="wide", initial_sidebar_state="collapsed")

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

st.markdown("""
    <style>
    .stApp {
        background-color: #bf7b5a;
        color: #ffffff;
    }
    
    .header {
        width: 100%;
        background-color: #ffae00;
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #ffffff33;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }

    .header-title {
        font-size: 1.8rem;
        font-weight: bold;
        color: white;
    }

    .nav-links a {
        margin-left: 30px;
        color: white;
        text-decoration: none;
        font-weight: 600;
        padding: 8px 16px;
        border-radius: 8px;
        background-color: #ffffff11;
        transition: 0.3s;
    }

    .nav-links a:hover {
        background-color: #ffffff33;
        color: #ffdd57;
    }

    .spacer {
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="header">
        <div class="header-title">📄 ResumAI</div>
        <div class="nav-links">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#tools">Tools</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    <div class="spacer"></div>
""", unsafe_allow_html=True)


st.markdown('<a name="home"></a>', unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center;">
        <h1>Welcome to ResumAI</h1>
        <p style="font-size: 18px;">
            Welcome to the AI-powered Resume Critiquer. <br>
            Upload your resume and optionally specify the job role you're targeting. <br>
            You'll receive actionable suggestions to improve your chances of landing interviews!
        </p>
            
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([2, 1])


with col1:
    st.markdown('<a name="about"></a>', unsafe_allow_html=True)
    st.subheader("🧠 About ResumAI")

    st.markdown("""
        ResumAI is an intelligent assistant designed to help students and professionals craft better resumes using artificial intelligence.

        It leverages Natural Language Processing (NLP) techniques and machine learning to:
        - ✅ Analyze and critique your resume content
        - 🎯 Ensure keyword optimization for ATS systems
        - 🧩 Provide tailored suggestions based on job roles
        - 📊 Score your resume across clarity, relevance, and formatting

        Whether you're applying for internships or jobs, ResumAI aims to make your resume **smarter, stronger, and more impactful**.
    """)

    


with col2:
    st.image("https://wpsstrapicms.cache.wpscdn.com/64_54db1031d2.png", width=1000)



st.markdown("---")
col3, col4 = st.columns([2, 1])


with col3:
    
    st.markdown('<a name="tools"></a>', unsafe_allow_html=True)
    st.subheader("🧰 Tools")

    # --- Resume Critiquer ---
    st.markdown("### 📝 Resume Critiquer")
    st.markdown("""
        This tool analyzes your resume content and layout.  
        It provides personalized suggestions to make your resume stand out, 
        match job descriptions, and improve clarity and professionalism.
    """)
        
    if st.button("🔍 Open Resume Critiquer"):
        st.switch_page("pages/critiquer.py")

    st.markdown("---")

    st.markdown("### 📊 Resume Scorer")
    st.markdown("""
        This tool gives your resume a score out of 100 based on various factors:  
        relevance, keyword match, readability, and formatting.  
        It's like an ATS (Applicant Tracking System) simulation.
    """)

    if st.button("📈 Check your Resume Score"):
        st.switch_page("pages/scorer.py")


with col4:
    st.image("https://cdn.prod.website-files.com/5e9b599e716f9d94b6c84f43/606faed39472eb276636b8f5_pdf-resume-template-format.png", width=1000)


# --- Footer ---
st.markdown("---")
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; font-size: 18px; line-height: 2;">
        <p>📞 <strong>Phone:</strong> 0333-0431520</p>
        <p>🔗 <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/uzair-majeed-605611319/" style="color: #ffffff;" target="_blank">linkedin.com/in/uzair-majeed</a></p>
        <p>🐙 <strong>GitHub:</strong> <a href="https://github.com/Uzair-Majeed" style="color: #ffffff;" target="_blank">github.com/Uzair-Majeed</a></p>
        <p>📧 <strong>Email:</strong> <a href="mailto:uzairmjd886@gmail.com" style="color: #ffffff;">uzairmjd886@gmail.com</a></p>
    </div>
""", unsafe_allow_html=True)


