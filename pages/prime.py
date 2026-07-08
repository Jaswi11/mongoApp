import streamlit as st
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
       st.warning("First Login !!!")
       st.stop()
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

st.title("python program code")
n=st.slider("pick a number",1,100)
f=0
for i in range(1,1+n):
    if n%i==0:
        f=f+1
if f==2:
    st.success("Prime")
else:
    st.success("not prime")
st.subheader("Python Code")
st.code('''
import streamlit as st
st.title("python program code")
n=st.slider("pick a number",1,100)
f=0
for i in range(1,1+n):
    if n%i==0:
        f=f+1
if f==2:
    st.success("Prime")
else:
    st.success("not prime")''')
