import streamlit as st
import time

st.set_page_config(page_title="CodeInsight GenAI", page_icon="⚡", layout="wide")

st.title("⚡ CodeInsight GenAI — App Test")
st.caption("IBM Generative AI Internship Project")

st.sidebar.header("🔑 Credentials")

# Toggle between Demo Mode and Live API Key
use_mock = st.sidebar.checkbox("Use Demo / Mock Mode (No API Key Required)", value=True)

if not use_mock:
    api_key = st.sidebar.text_input("Enter API Key", type="password")
else:
    st.sidebar.info("Demo Mode Active: Simulating AI responses.")
    api_key = "DEMO_KEY"

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Code")
    user_code = st.text_area(
        "Paste code snippet:",
        height=250,
        value="""def calculate_user_metrics(users):
    avg_score = sum(user['score'] for user in users) / len(users)
    SECRET_TOKEN = "sk-1234567890abcdef"
    return avg_score"""
    )
    
    task = st.selectbox("Task", ["Explain Code", "Find Bugs & Security Issues", "Refactor Code"])
    submit = st.button("🚀 Run Analysis", type="primary", use_container_width=True)

with col2:
    st.subheader("Output")
    if submit:
        if not use_mock and not api_key.strip():
            st.error("Please enter an API key or enable Demo Mode in the sidebar.")
        elif not user_code.strip():
            st.warning("Please paste some code first.")
        else:
            with st.spinner("Analyzing code..."):
                time.sleep(1.5)  # Simulates network request
                
                st.success("Analysis Complete!")
                
                if task == "Explain Code":
                    st.markdown("### 📝 Code Explanation")
                    st.write("This function takes a list of user dictionaries and calculates the average score across all users.")
                elif task == "Find Bugs & Security Issues":
                    st.markdown("### ⚠️ Bugs & Vulnerabilities")
                    st.warning("**ZeroDivisionError**: `len(users)` will crash if the input list is empty.")
                    st.error("**Security Risk**: Hardcoded `SECRET_TOKEN` found on line 4.")
                elif task == "Refactor Code":
                    st.markdown("### ⚡ Suggested Refactoring")
                    st.code("""def calculate_user_metrics(users: list) -> float:
    if not users:
        return 0.0
    return sum(user.get('score', 0) for user in users) / len(users)""", language="python")
    else:
        st.info("Click **Run Analysis** to test the response.")
