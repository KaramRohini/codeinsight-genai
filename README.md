# 🤖 CodeInsight GenAI

An automated code review and security analysis application powered by Google Gemini AI and Streamlit. Built for the IBM AI/ML Internship Capstone Project.

🚀 **Live App:** [https://codeinsight-genai-25xmcpc7fektwpdgjzys3t.streamlit.app](https://codeinsight-genai-25xmcpc7fektwpdgjzys3t.streamlit.app)

---

### ✨ Features
- **Bug & Security Detection:** Scans code for vulnerabilities, hardcoded secrets, and runtime risks.
- **Code Explanation:** Generates human-readable breakdowns of code logic.
- **Optimization & Refactoring:** Suggests clean, production-ready code replacements.
- **Unit Test Generation:** Automated creation of starter unit tests.

---

### 🛠️ Tech Stack
- **Frontend/UI:** Streamlit
- **AI Model Integration:** `google-generativeai` (`gemini-3.6-flash`)
- **Language:** Python 3.10+
- **Deployment:** Streamlit Community Cloud

---

### ⚙️ Local Setup Instructions
1. Clone the repository:
   ```bash
   git clone [https://github.com/KaramRohini/codeinsight-genai.git](https://github.com/KaramRohini/codeinsight-genai.git)
   pip install -r requirements.txt
   streamlit run app.py
   
