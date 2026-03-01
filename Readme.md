# Resume vs Job Description Matcher (Semantic AI + LLM)

## Project Overview

The **Resume vs Job Description Matcher** is an AI-powered NLP application that compares a candidate’s resume with a job description and evaluates how well they match.
The system uses **semantic embeddings + cosine similarity + LLM reasoning** to generate a realistic match score along with missing skills and improvement suggestions.

This project simulates a simplified **ATS (Applicant Tracking System)** used by companies to filter resumes.

---

## Features

* Compare resume and job description using **semantic similarity**
* Generate **match score**
* Identify **missing skills**
* Provide **improvement suggestions**
* Uses **LLM for intelligent feedback**
* Built with **Streamlit UI**
* Uses **free OpenRouter LLM models**
* Uses **Sentence Transformers for embeddings**

---

## Concepts Used

This project demonstrates real-world NLP + LLM workflow:

```
Text → Embeddings → Cosine Similarity → Score → LLM Feedback

---

## Tech Stack

| Component   | Technology            |
| ----------- | --------------------- |
| UI          | Streamlit             |
| Embeddings  | sentence-transformers |
| Similarity  | scikit-learn          |
| LLM API     | OpenRouter            |
| Model       | Llama 3.3 70B (free)  |
| Environment | python-dotenv         |
| Language    | Python                |
| Deployment  | Streamlit Cloud       |

---

## Installation

### 1. Clone repository

```
git clone https://github.com/Divyabansal20/AI_JD_Matcher.git
cd AI_JD_Matcher

```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Create .env file

```
OPENROUTER_API_KEY=your_api_key_here
```

Get API key from:

https://openrouter.ai

---

### 5. Run project

```
streamlit run app.py
```
---

## 👩‍💻 Author

Divya Bansal
B.Tech Computer Science (Data Science)
AI / NLP / Data Science Projects

GitHub: https://github.com/Divyabansal20

---
