import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="AI Fitness Activity Recognition")

st.title("🏋️ AI-Based Fitness Activity Recognition")

st.write("Upload sensor data to predict fitness activity")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(data.head())

    st.info("⚠️ Model file not added yet. This is UI demo.")

    st.success("Predicted Activity: Walking (Demo)")

st.sidebar.title("About")
st.sidebar.write(
    "AI-based fitness activity recognition using HAR dataset and Streamlit GUI."
)
