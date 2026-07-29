import streamlit as st
import pymongo
import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("sahujaswi@gmail.com","lubwoaufzytnniez")
conn=pymongo.MongoClient("mongodb+srv://jaswi11:jaswi123@cluster0.9g8j2lr.mongodb.net/?appName=Cluster0")
mydb=conn["ojt"]
my=mydb["user_info"]
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #BFEAF5 100%  /* Light Blue */
    );
}

/* Optional: Style the title */
h1 {
    color: white;
    text-align: center;
}

/* Optional: Style buttons */
.stButton > button {
    background-color: #144272;
    color: white;
    border-radius: 10px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.title("🔐CREATE ACCOUNT")
t1=st.text_input("username")
t2=st.text_input("password",type="password")
t3=str(st.text_input("Mobile number"))
t4=st.text_input("email ID")
t5=st.date_input("DOB")
b1=st.button("🔑SIGN IN ")
if b1:
    my.insert_one({"username":t1,"password":t2,"mobile":str(t3),"email":t4,"dob":str(t5)});
    server.sendmail("sahujaswi@gmail.com",t4,"HELLO WELCOME TO BASIC PYTHON LEARNING PLATFORM")
    st.success(f"Check the notification on email:{t4}") 
    st.success("🎉Sign Up Successfully")
                
    
                             
