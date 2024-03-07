import streamlit as st
import os

# Retrieve the API key from the environment variable
api_key = API_KEY


# Check if the API key is present
if api_key is None:
    st.error("API key not found. Please set the API_KEY environment variable.")
else:
    # Use the API key in your Streamlit app
    st.write("API key found:", api_key)
    # Add your code here to use the API key in your app as needed
