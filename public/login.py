import streamlit as st

# Auxiliary functions for autentication
def on_click():
    import time
    if st.session_state["correct_password"]:
        st.session_state["admin_view"] = True
        time.sleep(.25)
        query_dict = {}
        st.experimental_set_query_params(**query_dict)        
    else:
        st.warning("Wrong username or password")

st.title("Login")
c1, c2, c3 = st.columns([2,2,1])
user = c1.text_input("Username:", "")
pswd = c2.text_input("Password:", "", type="password")

try:
    USER = st.secrets["USER"]
    PASSWORD = st.secrets["PASSWORD"]
    if user==USER and pswd==PASSWORD:
        st.session_state["correct_password"] = True
    else:
        st.session_state["correct_password"] = False
    c3.markdown("")
    c3.markdown("")
    c3.button("Check", on_click=on_click)
except Exception as e:
    st.exception(e)



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