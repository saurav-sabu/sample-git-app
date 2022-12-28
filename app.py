import streamlit as st

st.title("Saurav Sabu Portfolio Website")

col1,col2 = st.columns(2)

with col1:
    st.image("dog.jpg")
with col2:
    st.write("""
    In late December 2022, an extratropical bomb cyclone brought blizzard conditions and winter storms to much of Canada and the United States, killing 72 people, causing vehicle pileups and road closures, and canceling or delaying more than 10,000 flights during the busy Christmas travel season. The storm was unofficially named Winter Storm Elliott by The Weather Channel. The National Weather Service in Buffalo, New York predicted this to be a "once-in-a-generation storm".[5][6][7]   
    """)


st.header("Courses Offered")

st.selectbox("Enter choice",["Data Science and Machine Learning","Data Analyst","Python","SQL","DSA"])

st.sidebar.title("Menu")
st.sidebar.markdown("""
- Home
- About
- Contact
- Career
- Login
""")