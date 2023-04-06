import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

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

#st.subheader("On a Scale of 1(Not Interested) to 6(Excellent), Rate Your Skills In The Following Subjects")

# def roundfigure(a):
#     x = int(a)
#     y = x+1
#     z = float((x+y)/2)
#     print(x,y,z)
#     import math
#     if(a<z):
#         n = math.floor(a)
#     else:
#         n = math.ceil(a)
#     return n


# Collects user input features into dataframe

def user_input_features():
    # g=st.radio("Enter gender",('Male','Female'))
    # a = st.text_input('Age')
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
    EXT1 = st.radio("1)I am the life of the party.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    EXT2 = st.radio("2)I don't talk a lot.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    EXT3 = st.radio("3)I feel comfortable around people.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    EXT4 = st.radio("4)I am quiet around strangers.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    EST1 = st.radio("5)I get stressed out easily.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    EST2 = st.radio("6)I get irritated easily.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    EST3 = st.radio("7)I worry about things.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    EST4 = st.radio("8)I change my mood a lot.",('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    AGR1 = st.radio("9)I have a soft heart.",('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    AGR2 = st.radio("10)I am interested in people.",('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    AGR3= st.radio("11)I insult people.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    AGR4 = st.radio("12)I am not really interested in others.",('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    CSN1= st.radio("13)I am always prepared.",('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    CSN2 = st.radio("14)I leave my belongings around.",('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    CSN3 = st.radio("15)I follow a schedule.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    CSN4 = st.radio("16)I make a mess of things.",('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    OPN1 = st.radio("17)I have a rich vocabulary.",('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    OPN2 = st.radio("18)I have difficulty understanding abstract ideas.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    OPN3 = st.radio("19)I do not have a good imagination.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    OPN4 = st.radio("20)I use difficult words.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    OTC=st.radio("21)I am afraid of change.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    HED=st.radio("22)I put worldly pleasures before productivity.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    STE1=st.radio("23)I feel connected to all living beings, including plants and animals.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    STE2=st.radio("24)I see a connection between who I am at all places and times.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    STE3=st.radio("25)I experience my self as more than my thoughts and feelings.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    STE4=st.radio("26)I am able to step back from my emotions and observe them from a separate point of view.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    CON=st.radio("27)I am capable of holding meaningful or respectful  conversations.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    EMO=st.radio("28)I have control over my emotions.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    SET1=st.radio("29)I am self-motivated and driven to continually improve myself.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    SET2=st.radio("30)I am willing to step outside of my comfort zone in order to challenge myself and grow.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    SET3=st.radio("31)I am open to constructive criticism and use it to improve myself.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))
    SET4=st.radio("32)I am proactive in seeking out opportunities for self-enhancement.", ('Strongly Disagree','Disagree','Slightly Disagree','Neutral','Slightly Agree','Agree','Strongly Agree'))

    d={"Strongly Disagree":1,"Slightly Disagree":2,"Disagree":3,"Neutral":4,"Agree":6,"Slightly Agree":5,"Strongly Agree":7}

    extraversion = 0
    #neuroticism = 0
    agreeableness = 0
    conscientiousness = 0
    openness = 0
    opennesstochange= d[OTC]/7
    hedonism= d[HED]/7
    selftranscendance= (d[STE1] + d[STE2] + d[STE3] + d[STE4])/28
    selfenhancement= (d[SET1] + d[SET2] + d[SET3] + d[SET4])/28
    conversation= d[CON]/7
    emotions=d[EMO]/7
    # gen=0
    extraversion = (d[EXT1] + d[EXT2] + d[EXT3] + d[EXT4])/28
    #neuroticism = (d[EST1] + d[EST2] + d[EST3] + d[EST4])/2.50
    agreeableness = (d[AGR1] + d[AGR2] + d[AGR3] + d[AGR4])/28
    conscientiousness = (d[CSN1] + d[CSN2] + d[CSN3] + d[CSN4])/28
    openness = (d[OPN1] + d[OPN2] + d[OPN3] + d[OPN4])/28
    # age=int(a)

    # if g=="Male":
    #     gen=1 
    # else:
    #     gen=0 

    # '''ext = roundfigure(extraversion)
    # #est = roundfigure(neuroticism)
    # agre = roundfigure(agreeableness)
    # csn = roundfigure(conscientiousness)
    # opn = roundfigure(openness) '''
    
    xyze = np.array([int(ques1),int(ques2),int(ques3),int(ques4),int(ques5),int(ques6),int(ques7),int(ques8),int(ques9),int(ques10),int(ques11),int(ques12),int(ques13),int(ques14),int(ques15),int(ques16),int(ques17)
    ,openness,conscientiousness,extraversion,agreeableness,emotions,conversation,opennesstochange,hedonism,selfenhancement,selftranscendance])
    xyze = xyze.reshape(1,-1) 
    return xyze 


st.write(user_input_features)

load_clf = pickle.load(open('lr_clf.pkl','rb'))
st.title("Role Predicition")
x = user_input_features()
prediction = load_clf.predict(x)
st.subheader("Predicition Probability")
prediction_proba= load_clf.predict_proba(x)
st.write(prediction_proba)
prediction_proba = np.array(prediction_proba)
st.bar_chart(prediction_proba)
# fig, ax = plt.subplots()
# ax.hist(prediction_proba)

# st.pyplot(fig)


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


    