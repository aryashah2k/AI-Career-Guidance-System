import streamlit as st
import streamlit_book as stb

st.title("Home")

st.markdown("""
This is where you should put your Home landing page.
Just edit the file `public/home.py`.
""")

st.markdown("""
This streamlit multipage template allows to have public pages and private pages.
* You can see it working at this link: https://stbook-template.streamlitapp.com/
* You can download it or fork it from this link: https://github.com/sebastiandres/template_streamlit_multipage
* Edit the pages, create more pages and edit the content to suit your needs!
""")

st.markdown("---")
st.subheader("Share the love!")
stb.share("Look at this cool streamlit template I found!", "https://stbook-template.streamlitapp.com/")