"""
Hemp Industry Economic Impact Dashboard
A data-driven resource for stakeholders and policymakers
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Hemp Industry Economic Impact",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Test if secrets are available
st.write("Checking secrets...")
try:
    if "gcp_service_account" in st.secrets:
        st.success("Secrets found!")
        st.write("Keys:", list(st.secrets["gcp_service_account"].keys()))
    else:
        st.error("No gcp_service_account in secrets")
        st.write("Available secrets:", list(st.secrets.keys()) if st.secrets else "None")
except Exception as e:
    st.error(f"Error reading secrets: {e}")

# Try BigQuery connection
st.write("Testing BigQuery connection...")
try:
    from google.cloud import bigquery
    from google.oauth2 import service_account

    credentials = service_account.Credentials.from_service_account_info(
        dict(st.secrets["gcp_service_account"])
    )
    client = bigquery.Client(credentials=credentials, project="artful-logic-475116-p1")

    # Test query
    query = "SELECT COUNT(*) as cnt FROM `artful-logic-475116-p1.hemp_advocacy.regulatory_status`"
    result = client.query(query).to_dataframe()
    st.success(f"BigQuery connected! Found {result['cnt'].iloc[0]} regulatory records")
except Exception as e:
    st.error(f"BigQuery error: {e}")
    st.stop()

st.write("If you see this, everything works!")
