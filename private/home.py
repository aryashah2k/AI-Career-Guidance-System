import streamlit as st
import streamlit_book as stb

st.title("My Career Recommendations")

st.markdown("Your Saved Careers Show Up Here!")

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