import google.generativeai as genai
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="CodeInsight GenAI", page_icon="💡", layout="wide"
)

st.title("💡 CodeInsight GenAI")
st.caption("IBM AI/ML Internship Capstone Project | Automated Code Reviewer")

st.markdown("---")

# Sidebar Configuration
st.sidebar.header("⚙️ Configuration")

# Retrieves key from Streamlit Secrets if available, otherwise expects user input
default_key = st.secrets.get("GEMINI_API_KEY", "")
api_key = st.sidebar.text_input(
    "Enter Gemini API Key",
    value=default_key,
    type="password",
    help="Get a free key from https://aistudio.google.com/",
)

task = st.sidebar.selectbox(
    "Select Analysis Task",
    [
        "Find Bugs & Security Vulnerabilities",
        "Explain Code",
        "Refactor & Optimize Code",
        "Generate Unit Tests",
    ],
)

model_choice = st.sidebar.selectbox(
    "Select Model", ["gemini-3.6-flash", "gemini-2.5-pro"]
)

# Main Interface Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Input Code Snippet")
    language = st.selectbox(
        "Programming Language",
        ["Python", "JavaScript", "Java", "C++", "SQL", "HTML/CSS"],
    )
    code_input = st.text_area(
    "Paste code to analyze:",
    value="",
    placeholder="Paste your code here...",
    height=320,
)
    code_input = st.text_area(
        "Paste code to analyze:", value=default_code, height=320
    )

    analyze_btn = st.button(
        "🚀 Analyze Code", type="primary", use_container_width=True
    )

with col2:
    st.subheader("GenAI Output & Recommendations")

    if analyze_btn:
        if not api_key.strip():
            st.error(
                "❌ Missing API Key! Please enter your Gemini API key in the sidebar."
            )
        elif not code_input.strip():
            st.warning("⚠️ Please paste code into the text box before analyzing.")
        else:
            with st.spinner("Analyzing code structure and security..."):
                try:
                    # Configure Gemini API
                    genai.configure(api_key=api_key.strip())
                    model = genai.GenerativeModel(model_choice)

                    prompt = f"""
                    You are an expert AI code reviewer and security analyzer.
                    Perform the task: '{task}' on the following {language} code snippet.

                    Structure your response with clear Markdown headings:
                    - **Summary**: Brief overview of the analysis.
                    - **Key Findings / Issues**: List bugs, performance bottlenecks, or security flaws.
                    - **Improved / Corrected Code**: Provide updated code block.
                    - **Best Practice Tips**: Concise suggestions for improvement.

                    Code:
                    ```{language.lower()}
                    {code_input}
                    ```
                    """

                    response = model.generate_content(prompt)

                    st.success("✅ Analysis Complete!")
                    st.markdown(response.text)

                except Exception as e:
                    st.error(f"🚨 API Request Failed: {str(e)}")
                    st.info(
                        "Tip: Double-check that your Gemini API key is active and correctly formatted."
                    )
    else:
        st.info(
            "Paste your code on the left and click **Analyze Code** to see real-time feedback."
        )

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>CodeInsight GenAI • Built with Streamlit & Gemini API</p>",
    unsafe_allow_html=True,
)
