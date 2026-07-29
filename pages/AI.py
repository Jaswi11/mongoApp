import streamlit as st
import pandas as pd

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Improved dataset
data = {
    "career": [
        "Web Developer",
        "AI Engineer",
        "Data Scientist",
        "UI/UX Designer",
        "Cyber Security Analyst",
        "Mobile App Developer",
        "Cloud Engineer",
        "Software Tester",
        "DevOps Engineer",
        "Business Analyst"
    ],
    
    "Required_Skill": [
        "html css javascript react nodejs",
        "python machine learning deep learning nlp tensorflow",
        "python statistics machine learning data visualization pandas",
        "figma design thinking ux research prototyping creativity",
        "network security ethical hacking cryptography linux",
        "flutter android ios kotlin java mobile development",
        "aws cloud computing docker kubernetes linux",
        "manual testing automation selenium bug tracking",
        "ci cd docker kubernetes aws scripting",
        "excel data analysis communication sql problem solving"
    ]
}

df = pd.DataFrame(data)

st.title("💼 AI Career Guidance System")
st.write("Enter your skills (comma separated):")
st.write(df)

# User input
user_input = st.text_area("Enter your skills")

if st.button("Get Career Recommendation"):

    if user_input.strip() == "":
        st.warning("Please enter your skills!")
    else:
        # Convert text to lowercase
        user_input = user_input.lower()

        # TF-IDF Vectorization
        vectorizer = TfidfVectorizer()
        skill_matrix = vectorizer.fit_transform(df["Required_Skill"])
        user_vector = vectorizer.transform([user_input])

        # Cosine Similarity
        similarity_scores = cosine_similarity(user_vector, skill_matrix).flatten()

        df["match_score"] = similarity_scores

        # Top 5 recommendation
        recommendation = df.sort_values(by="match_score", ascending=False).head(5)

        st.subheader("🔍 Top Career Matches")
        st.table(recommendation[["career", "match_score"]])

        # Pie Chart
        labels = recommendation["career"]
        sizes = recommendation["match_score"]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        st.subheader("📊 Career Match Distribution")
        st.pyplot(fig)
