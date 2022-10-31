import streamlit as st

st.title("Logout")

st.markdown("Click to logout")

def on_click():
    import time
    st.session_state["admin_view"] = False
    st.success("Logged out")
    time.sleep(.25)
    query_dict = {}
    st.experimental_set_query_params(**query_dict)

st.button("Logout", on_click=on_click)
