import streamlit as st
import streamlit_book as stb

# hide_menu_style = """
#         <style>        #MainMenu {visibility: hidden;}
#         </style>        """
# st.markdown(hide_menu_style, unsafe_allow_html=True)\


# st.markdown(hide_streamlit_style, unsafe_allow_html=True)




page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Leather_notebook_%28Unsplash%29.jpg/2560px-Leather_notebook_%28Unsplash%29.jpg");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Leather_notebook_%28Unsplash%29.jpg/2560px-Leather_notebook_%28Unsplash%29.jpg");
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

st.markdown("<h1 style='text-align: LEFT; font-family: Georgia; color: black; font-size: 15px'>WELCOME TO,</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: LEFT; font-family: Georgia; color: black; font-size: 40px'>AI BASED CAREER GUIDANCE SYSTEM</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("<p style='text-align: LEFT; font-family: Garamond; color: black; font-size: 20px'> We understand the struggle of finding the right career..<br>There are just too many options and too many factors to consider!<br>But dont you worry, we are here to help :)<br>Learn about different careers with our career exploration tool <br>and find the right career with our career recommendation quiz.</p>", unsafe_allow_html=True)

