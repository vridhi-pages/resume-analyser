import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key= "AIzaSyBAsAdiHYQxkv4kYhO94aoK3xq2qbcB5QQ")


def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt = r"""
Hey! Act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of the tech field, software engineering, data science, data analysis, and big data engineering. Your task is to evaluate the resume based on the given job description. You must consider the job market is very competitive and you should provide the best assistance for improving the resumes. Assign the percentage matching based on JD and the missing keywords with high accuracy.
Assign the percentage Matching based on Jd and the missing keywords with high accuracy
Strictly use the resume:{text}, description:{jd} content only to give the response and stick to the format provided below.

**JD Match:** {jd_match}%
**Missing Keywords:** {missing_keywords}
**Profile Summary:** {profile_summary}
**Improvement Areas:** {improvement_areas}


**Resume Score:** {resume_score}
**Resume Readability:** {resume_readability}
**Resume Length:** {resume_length}
**Resume Format:** {resume_format}
**Resume Font Score:** {resume_font_score}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)