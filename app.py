from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd
from utils.csv_parser import parse_csv
from utils.code_engine import run_analysis
from utils.chart_generator import generate_chart
from utils.insight_narrator import narrate_insights

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Data Analyst")
st.caption("Upload a CSV · Ask questions · Get instant insights")

# --- Session state ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "df" not in st.session_state:
    st.session_state.df = None
if "csv_summary" not in st.session_state:
    st.session_state.csv_summary = None

# --- Sidebar: File Upload ---
with st.sidebar:
    st.header("📁 Upload Your Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file:
        df, summary = parse_csv(uploaded_file)
        st.session_state.df = df
        st.session_state.csv_summary = summary
        st.success(f"✅ Loaded: {summary['rows']} rows × {summary['cols']} columns")
        st.json(summary, expanded=False)

    st.divider()
    st.markdown("**Example questions:**")
    st.markdown("- What are the top 5 categories by sales?")
    st.markdown("- Show me the monthly trend")
    st.markdown("- Are there any outliers?")
    st.markdown("- Summarise this dataset")

# --- Chat history ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "chart" in msg:
            st.plotly_chart(msg["chart"], use_container_width=True)

# --- Chat input ---
if prompt := st.chat_input("Ask anything about your data..."):
    if st.session_state.df is None:
        st.warning("Please upload a CSV file first.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Analysing..."):
                df = st.session_state.df
                summary = st.session_state.csv_summary

                analysis_result = run_analysis(df, summary, prompt)
                chart = generate_chart(df, prompt, analysis_result)
                narrative = narrate_insights(prompt, analysis_result, summary)

                st.markdown(narrative)
                if chart:
                    st.plotly_chart(chart, use_container_width=True)

        msg_data = {"role": "assistant", "content": narrative}
        if chart:
            msg_data["chart"] = chart
        st.session_state.messages.append(msg_data)