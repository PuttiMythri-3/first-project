import streamlit as st
import pandas as pd
st.title("hello world")
st.header("second")
st.subheader("mrecw")
st.write("streamlit")
st.text_input("enter your name")
st.number_input("enter your age")
st.text_area("enter address")
st.slider("select your age",0,100)
st.checkbox("i agree")
options=st.selectbox("select an option",["opt1","opt2","opt3"])
st.write("you selected:",options)
st.radio("select gender",["male","female","other"])
st.sidebar.title("sidebar")
st.sidebar.text_input("enter your name")
st.sidebar.number_input("enter your age")
st.sidebar.text_area("enter address")
st.sidebar.slider("select your age",0,100)
st.sidebar.checkbox("i agree")
options=st.sidebar.selectbox("select an option",["opt1","opt2","opt3"])
st.sidebar.write("you selected:",options)
st.markdown("***bold***")
st.markdown("*india*")
st.markdown("#heading1#")
st.markdown("##heading2##")
st.markdown("###heading3###")
st.write("[google](https://www.google.com)")
st.balloons()
st.snow()
st.title("File Upload Example")


with st.form("Form"):
    col1,col2=st.columns(2)
    fname=col1.text_input("First Name")
    lname=col2.text_input("Last Name")
    email=st.text_input("Enter your email")
    password=st.text_input("Enter Password")
    confirm_pwd=st.text_input("Confirm Password")
    c1,c2=st.columns(2)
    sdate=c1.date_input("Start date")
    ldate=c2.date_input("Last date")
    submit=st.form_submit_button("Submit")
if submit:
    st.write(fname)
uploaded_file = st.file_uploader("Upload a file")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
df=pd.read_csv("data.csv")
st.write(df)
    


