import streamlit as st
import page1
import page2
import page3
import page4

PAGES = {
    'Introduction': page1,
    'CV': page2
}

st.sidebar.title('Hello World!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
