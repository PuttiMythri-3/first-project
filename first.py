import streamlit as st
tab1,tab2,tab3=st.tabs(["tab1","tab2","tab3"])
with tab1:
        st.write("content 1")
        st.text_input("enter your name in tab1")
with tab2:
        st.write("content 2")
        st.text_input("enter your name in tab2")
with tab3:
        st.write("content 3")
        st.text_input("enter your name in tab3")
