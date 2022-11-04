import streamlit as st
import streamlit_book as stb
import numpy as np
import pandas as pd
import webbrowser
from PIL import Image
from itertools import cycle

st.markdown("<h1 style='text-align: center; font-family: 'Times New Roman', serif; color: black; font-size: 550px'><u>Explore Careers<u></h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://iili.io/bk2duf.md.png");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://iili.io/bk2duf.md.png");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown(page_bg_img, unsafe_allow_html=True)

with st.container():
     col1, col2, col3 = st.columns(3)
     with col1:
         
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Symbol_tick_plus_blue.svg/320px-Symbol_tick_plus_blue.svg.png)](https://www.simplilearn.com/quality-engineer-article)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**Quality Analyst**") 
     with col2:
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Severed_video_game_logo.png/320px-Severed_video_game_logo.png)](https://www.simplilearn.com/how-to-become-a-game-developer-article)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**Game Developer**") 
     with col3:
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Responsive_Web_Design_Demo_Template.svg/320px-Responsive_Web_Design_Demo_Template.svg.png)](https://www.simplilearn.com/how-to-become-a-front-end-developer-article)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;**Front-end Developer**") 

with st.container():
     col1, col2, col3 = st.columns(3)
     with col1:
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/%28EPA_Science_Aspect_2%29_412-DSP-2-2012-08-07_AspectTX_026.jpg_-_DPLA_-_417886293932aa1f2fe8a2ea8d8b9d97.jpg/320px-%28EPA_Science_Aspect_2%29_412-DSP-2-2012-08-07_AspectTX_026.jpg_-_DPLA_-_417886293932aa1f2fe8a2ea8d8b9d97.jpg)](https://www.simplilearn.com/how-to-become-a-software-engineer-article)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;**Software Developer**") 
         
     with col2:
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/UX_Design_Concept_Illustration.jpg/320px-UX_Design_Concept_Illustration.jpg)](https://www.simplilearn.com/how-to-become-ui-ux-designer-article)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**UX Designer**") 
     with col3:
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Data_citation.jpg/320px-Data_citation.jpg)](https://www.simplilearn.com/tutorials/data-science-tutorial/how-to-become-a-data-scientist)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**Data Scientist**") 
         

with st.container():
     col1, col2, col3 = st.columns(3)
     with col1:
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Defense_Secretary_Ash_Carter_tours_the_Microsoft_Cybercrime_Center_in_Seattle%2C_March_3%2C_2016.JPG/320px-Defense_Secretary_Ash_Carter_tours_the_Microsoft_Cybercrime_Center_in_Seattle%2C_March_3%2C_2016.JPG)](https://www.simplilearn.com/tutorials/cyber-security-tutorial/how-to-become-cyber-security-engineer)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;**Cybersecurity Specialist**") 
     with col2:
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Fundamentals_of_Business_-_Fig._2.1_-_Circular_flow_of_inputs_and_outputs.jpg/320px-Fundamentals_of_Business_-_Fig._2.1_-_Circular_flow_of_inputs_and_outputs.jpg)](https://www.simplilearn.com/tutorials/business-analysis-tutorial/how-to-become-a-business-analyst)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;**Business Analyst**") 
     with col3:
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Maker_Faire%2C_Berlin_%28BL7C0161%29.jpg/320px-Maker_Faire%2C_Berlin_%28BL7C0161%29.jpg)](https://www.simplilearn.com/how-to-become-a-robotics-engineer-article)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;**Robotics Engineer**")
         

with st.container():
     col1, col2, col3 = st.columns(3)
     with col1:
          
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Scheda_Audio.png/285px-Scheda_Audio.png)](simplilearn.com/career-in-it-hardware-and-networking-article)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;**Hardware Engineer**")  
     with col2:
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/AWS_Simple_Icons_Database_Amazon_RDS_MySQL_DB_Instance.svg/240px-AWS_Simple_Icons_Database_Amazon_RDS_MySQL_DB_Instance.svg.png)](https://www.computerscience.org/careers/database-administrator/#:~:text=Database%20administrators%20need%20at%20least,database%20administration%20or%20information%20technology.)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;**Database Administrator**") 
     with col3:
          st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Programming_code.jpg/320px-Programming_code.jpg)](https://www.simplilearn.com/how-to-become-a-backend-developer-article)")
          st.markdown("&emsp;&emsp;&emsp;&emsp;&emsp;**Backend Developer**") 

