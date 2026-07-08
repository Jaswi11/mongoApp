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

st.title("Odd_even")
num = st.slider("Select a number",0,100)
if num % 2 == 0:
    st.success(f"{num} is an Even number.")
else:
    st.success(f"{num} is an Odd number.")
st.header("Python Code")
st.code('''
import streamlit as st
st.title("Odd_even")
num = st.slider("Select a number",0,100)
if num % 2 == 0:
    st.success(f"{num} is an Even number.")
else:
    st.success(f"{num} is an Odd number.")''')
