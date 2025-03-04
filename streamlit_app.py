import streamlit as st
import requests

API_BASE_URL = "https://v6api.onrender.com"

st.title("Escalytics V6 R1 API")

st.sidebar.title("Options")
option = st.sidebar.selectbox("Choose an option", ["Generate Insights", "Analyze Attachment", "Extract Metadata", "Download Report"])

if option == "Generate Insights":
    st.header("Generate Insights")
    email_content = st.text_area("Email Content", height=200)
    features = {
        "highlights": st.checkbox("Highlights"),
        "response": st.checkbox("Response"),
        "tone": st.checkbox("Tone"),
        "task_extraction": st.checkbox("Task Extraction"),
        "subject_recommendation": st.checkbox("Subject Recommendation"),
        "clarity": st.checkbox("Clarity"),
        "complexity_reduction": st.checkbox("Complexity Reduction"),
        "scenario_responses": st.checkbox("Scenario Responses"),
        "phishing_detection": st.checkbox("Phishing Detection"),
        "sensitive_info_detection": st.checkbox("Sensitive Info Detection"),
        "confidentiality_rating": st.checkbox("Confidentiality Rating"),
        "bias_detection": st.checkbox("Bias Detection"),
        "conflict_detection": st.checkbox("Conflict Detection"),
        "argument_mining": st.checkbox("Argument Mining")
    }
    scenario = st.text_input("Scenario")

    if st.button("Generate Insights"):
        payload = {
            "email_content": email_content,
            "features": features,
            "scenario": scenario
        }
        response = requests.post(f"{API_BASE_URL}/generate_insights", json=payload)
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Error generating insights")

elif option == "Analyze Attachment":
    st.header("Analyze Attachment")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        files = {'file': uploaded_file.getvalue()}
        response = requests.post(f"{API_BASE_URL}/analyze_attachment", files=files)
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Error analyzing attachment")

elif option == "Extract Metadata":
    st.header("Extract Metadata")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        files = {'file': uploaded_file.getvalue()}
        response = requests.post(f"{API_BASE_URL}/extract_metadata", files=files)
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Error extracting metadata")

elif option == "Download Report":
    st.header("Download Report")
    data = st.text_area("Data (JSON format)", height=200)
    if st.button("Download Report"):
        payload = json.loads(data)
        response = requests.post(f"{API_BASE_URL}/download_report", json=payload)
        if response.status_code == 200:
            st.download_button("Download Report", response.content, file_name="analysis.pdf")
        else:
            st.error("Error downloading report")
