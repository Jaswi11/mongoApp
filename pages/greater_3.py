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

st.title("Greatest of Three Numbers")
num1 = st.slider("Select First Number", 0, 100, 10)
num2 = st.slider("Select Second Number", 0, 100, 20)
num3 = st.slider("Select Third Number", 0, 100, 30)
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3
st.success(f"The greatest number is {greatest}")
st.header("Python code")
st.code('''
import streamlit as st
st.title("Greatest of Three Numbers")
num1 = st.slider("Select First Number", 0, 100, 10)
num2 = st.slider("Select Second Number", 0, 100, 20)
num3 = st.slider("Select Third Number", 0, 100, 30)
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3
st.success(f"The greatest number is {greatest}")''')
