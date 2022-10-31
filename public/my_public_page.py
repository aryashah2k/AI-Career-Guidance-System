import streamlit as st
import streamlit_book as stb
import numpy as np
import pandas as pd

st.title("My Public Page")

st.markdown("This is where you put your public content. This file is 'public/my_public_page.py'.")

st.markdown("""
* Copy and rename as many files as needed.
* Edit streamlit_app.py to include the files as pages!
""")

st.subheader("Maybe some data")
N = 10
df = pd.DataFrame(100*np.random.randn(5, N), columns=('col%d' % i for i in range(N)))
st.dataframe(df)  # Same as st.write(df)

st.subheader("Maybe some plots")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.subheader("Maybe some interactive activities")
stb.true_or_false(
                    'Is "Indiana Jones and the Last Crusade" the best movie of the trilogy?', 
                    True, 
                    success="You have chosen wisely", 
                    error="You have chosen poorly", 
                    button="You must choose"
                )