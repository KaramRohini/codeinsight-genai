import streamlit as st

st.set_page_config(page_title="CodeInsight GenAI", page_icon="🤖", layout="wide")

st.title("🤖 CodeInsight GenAI")
st.caption("IBM AI/ML Internship Capstone Project | Automated Code Reviewer")

st.sidebar.header("⚙️ Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
lang = st.sidebar.selectbox("Language", ["Python", "JavaScript", "C++", "Java", "SQL"])
review_mode = st.sidebar.radio("Focus", ["Bug Detection & Fix", "Security Vulnerabilities", "Code Optimization"])

code_input = st.text_area("Paste code here:", height=200, placeholder="def example():\n    pass")

if st.button("🚀 Analyze Code", type="primary"):
    if not api_key:
        st.error("⚠️ Please enter your Gemini API Key in the sidebar.")
    elif not code_input.strip():
        st.warning("⚠️ Please paste some code to analyze.")
    else:
        with st.spinner("Analyzing code..."):
            try:
                from google import genai
                client = genai.Client(api_key=api_key)
                prompt = f"You are a Senior Code Auditor. Review this {lang} code with focus on '{review_mode}':\n\n```\n{code_input}\n```"
                response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                
                st.subheader("💡 Code Review & Refactored Output")
                st.markdown(response.text)
                st.success("✅ Analysis Complete!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")