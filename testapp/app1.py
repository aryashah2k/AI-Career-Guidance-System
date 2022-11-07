import streamlit as st
import pandas as pd
import numpy as np
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

st.subheader("On a Scale of 1(Not Interested) to 6(Excellent), Rate Your Skills In The Following Subjects")



# Collects user input features into dataframe

def user_input_features():

    ques1 = st.selectbox("1) Database Fundamentals", ('1', '2', '3', '4', '5',"6"))
    ques2 = st.selectbox("2) Computer Architecture", ('1', '2', '3', '4', '5',"6"))
    ques3 = st.selectbox("3) Distributed Computing Systems", ('1', '2', '3', '4', '5',"6"))
    ques4 = st.selectbox("4) Cyber Security", ('1', '2', '3', '4', '5',"6"))    
    ques5 = st.selectbox("5) Computer Networks", ('1', '2', '3', '4', '5',"6"))
    ques6 = st.selectbox("6) Software Development", ('1', '2', '3', '4', '5',"6"))
    ques7 = st.selectbox("7) Programming Skills", ('1', '2', '3', '4', '5',"6"))
    ques8 = st.selectbox("8) Project Management", ('1', '2', '3', '4', '5',"6"))
    ques9 = st.selectbox("9) Computer Forensics Fundamentals", ('1', '2', '3', '4', '5',"6"))
    ques10 = st.selectbox("10) Technical Communication", ('1', '2', '3', '4', '5',"6"))
    ques11 = st.selectbox("11) AI/ML", ('1', '2', '3', '4', '5',"6"))
    ques12 = st.selectbox("12) Software Engineering", ('1', '2', '3', '4', '5',"6"))
    ques13 = st.selectbox("13) Business Analysis", ('1', '2', '3', '4', '5',"6"))
    ques14 = st.selectbox("14) Communication Skills", ('1', '2', '3', '4', '5',"6"))
    ques15 = st.selectbox("15) Data Science", ('1', '2', '3', '4', '5',"6"))
    ques16 = st.selectbox("16) Troubleshooting Skills", ('1', '2', '3', '4', '5',"6"))
    ques17 = st.selectbox("17) Graphics Designing", ('1', '2', '3', '4', '5',"6"))

    data = {'Database Fundamenatals': ques1,
            'Computer Architecture': ques2,
            'Distributed Computing Systems': ques3, 
            'Cyber Security': ques4,
            'Computer Networks':ques5,
            'Software Development': ques6,
            'Programming Skills': ques7,
            'Project Management': ques8,
            'Computer Forensics Fundamentals':ques9,
            'Technical Communication':ques10,
            'AI ML':ques11,
            'Software Engineering':ques12,
            'Business Analysis':ques13,
            'Communication Skills':ques14,
            'Data Science':ques15,
            'Troubleshooting Skills':ques16,
            'Graphics Designing':ques17
                }
    features = pd.DataFrame(data, index=[0])
    return features
    # features = pd.DataFrame.to_numpy(data)

input_df = user_input_features()

st.write(input_df)

load_clf = pickle.load(open('bestmodel.pkl','rb'))
st.title("Role Predicition")
prediction = load_clf.predict(input_df)
# st.subheader("Predicition Probability")
# prediction_proba= load_clf.predict_proba(input_df)

if prediction == 0:
    pred = 'AI ML Specialist'
elif prediction ==1:
    pred = 'API Specialist'
elif prediction ==2:
    pred = 'Application Support Engineer'
elif prediction ==3:
    pred = 'Business Analyst'
elif prediction ==4:
    pred = 'Customer Service Executive'
elif prediction ==5:
    pred = 'Cyber Security Specialist'
elif prediction ==6:
    pred = 'Data Scientist'
elif prediction ==7:
    pred = 'Database Administrator'
elif prediction ==8:
    pred = 'Graphics Designer'
elif prediction ==9:
    pred = 'Hardware Engineer'
elif prediction ==10:
    pred = 'Helpdesk Engineer'
elif prediction ==11:
    pred = 'Information Security Specialist'
elif prediction ==12:
    pred = 'Networking Engineer'
elif prediction ==13:
    pred = 'Project Manager'
elif prediction ==14:
    pred = 'Software Developer'
elif prediction ==15:
    pred = 'Software tester'
elif prediction ==16:
    pred ='Technical Writer'

st.subheader(pred)


    