import streamlit as st

st.title("Logout")

st.markdown("Are You Sure You Want To Logout?")

def on_click():
    import time
    st.session_state["admin_view"] = False
    st.success("Logged out")
    time.sleep(.25)
    query_dict = {}
    st.experimental_set_query_params(**query_dict)

st.button("Yes", on_click=on_click)

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