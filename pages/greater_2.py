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

st.title("Greater Number Finder")
num1 = st.slider("Select First Number",0,100)
num2 = st.slider("Select Second Number",0,100)
if num1 > num2:
    st.success(f"{num1} is greater than {num2}.")
elif num2 > num1:
    st.success(f"{num2} is greater than {num1}.")
else:
    st.info("Both numbers are equal.")
st.header("Python code")
st.code('''
import streamlit as st
st.title("Greater Number Finder")
num1 = st.slider("Select First Number",0,100)
num2 = st.slider("Select Second Number",0,100)
if num1 > num2:
    st.success(f"{num1} is greater than {num2}.")
elif num2 > num1:
    st.success(f"{num2} is greater than {num1}.")
else:
    st.info("Both numbers are equal.")''')
