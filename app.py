import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
from openai import OpenAI
from dotenv import load_dotenv



model = SentenceTransformer("all-MiniLM-L6-v2")
load_dotenv()
api_key= os.getenv("OPENROUTER_API_KEY")

client= OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

st.title("Resume vs Job Description Matcher")

st.write("Compare your resume with a job description")

resume_text = st.text_area(
    "Paste your Resume",
    height=200
)

jd_text = st.text_area(
    "Paste Job Description",
    height=200
)

if st.button("Match"):
    if resume_text and jd_text:
        embed1= model.encode(resume_text)
        embed2= model.encode(jd_text)
        similarity=cosine_similarity([embed1],[embed2])
        st.write("Similarity score: ",similarity[0][0])

        response= client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct",
            messages=[
                {"role":"system",         "content": "You are an AI recruiter. Compare resume with job description carefully and give realistic feedback like an ATS system."
},
                
                {"role":"user", "content":
                 f"""
Resume text: {resume_text},
JD Text: {jd_text},
score:{similarity[0][0]},
Instructions:
1. Explain match level
2. List matching skills
3. List missing skills
4. Give suggestions to improve resume
5. Be realistic for a student-level candidate"""
                }
            ],
            max_tokens=400
        )
        st.subheader("AI Feedback")
        st.write(response.choices[0].message.content)

    else:
        st.warning("Write both, resume text and jd text!")
