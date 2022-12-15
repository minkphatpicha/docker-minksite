import streamlit as st
import page1
import page2
import page3

PAGES = {
    'Introduction': page1,
    'CV': page2,
    'Page 3': page3
}

st.sidebar.title('Hello World!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
