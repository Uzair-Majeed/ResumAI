
# ResumAI 📝
# Link : https://resumai-io.streamlit.app/

ResumAI is an AI-powered resume analyzer built using Streamlit and OpenRouter API. It provides personalized feedback and scoring on resumes based on content clarity, relevance, formatting, and keyword optimization.

## 🚀 Features

- **Resume Critiquer**: Upload your resume and receive AI-generated suggestions for improvement.
- **Resume Scorer**: Receive a score out of 100 based on relevance, clarity, keywords, and formatting.
- **Beautiful UI**: Fully styled interface with hidden sidebar for a clean experience.
- **One-click Navigation**: Use `streamlit-extras` for smooth page switching.

## 📦 Installation

Ensure you have Python installed, then use [`uv`](https://github.com/astral-sh/uv) or `pip` to install dependencies.

```bash
uv venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -r requirements.txt
```

## 🔧 Environment Setup

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

## ▶️ Running the App

```bash
streamlit run app.py
```

## 🧾 File Structure

```
Resume_Critiquer/
├── app.py              # Main homepage
├── pages/
│   ├── critiquer.py    # Resume Critique page
│   └── scorer.py       # Resume Score page
├── .env
├── README.md
└── requirements.txt
```

## 📄 License

This project is open-source and free to use under the MIT License.

## 👤 Author

- Uzair Majeed  
- [LinkedIn](https://www.linkedin.com/in/uzair-majeed-605611319/)  
- [GitHub](https://github.com/Uzair-Majeed)
