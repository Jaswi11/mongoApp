import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb+srv://jaswi11:jaswi123@cluster0.9g8j2lr.mongodb.net/?appName=Cluster0")
mydb=conn["ojt"]
my=mydb["user_info"]
st.title("🐍ALL BASIC PYTHON CODE")
t1=st.text_input("username")
t2=st.text_input("password",type="password")
b=st.button("🔑SIGN IN")
valid=0
if b:
    ans= my.find({"username":t1,"password":t2}  )
    for i in ans:
        valid=valid+1
        st.session_state["username"]=i['username']
        st.session_state["password"]=i['password']
        st.switch_page("pages/3profile.py")
    if valid==0:
        st.success("Invalid User Login Details")
