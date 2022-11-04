import streamlit as st
import streamlit_book as stb
import numpy as np
import pandas as pd
import time
import pickle

def add_bg_from_url(): 
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://iili.io/bk2duf.md.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

st.title("Career Role Prediction")

st.subheader("Attempt The Following Questionaire For The AI To Predict The Best Role For You.")

st.markdown("Rate Your Skills In The Following Subjects")

ques1 = st.radio("1) Computer Architecture", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques2 = st.radio("2) Distributed Computing Systems", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques3 = st.radio("3) Cyber Security", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))    
ques4 = st.radio("4) Computer Networks", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques5 = st.radio("5) Software Development", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques6 = st.radio("6) Programming Skills", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques7 = st.radio("7) Project Management", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques8 = st.radio("8) Computer Forensics Fundamentals", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques9 = st.radio("9) Technical Communication", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques10 = st.radio("10) AI/ML", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques11 = st.radio("11) Software Engineering", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques12 = st.radio("12) Business Analysis", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques13 = st.radio("13) Communication Skills", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques14 = st.radio("14) Data Science", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques15 = st.radio("15) Troubleshooting Skills", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))
ques16 = st.radio("16) Graphics Designing", ('Not Interested', 'Poor', 'Beginner', 'Average', 'Intermediate',"Excellent"))

result = ""

if st.button("Get Recommendation"):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.03)
                progress.progress(i + 1)
            st.balloons()
            result = st.markdown("Work In Progress! Check Back Later !!!")
       

