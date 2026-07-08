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

st.title("Multiplication Table Generator")
num = st.slider("Select a Number", 1, 20, 5)
st.subheader(f"Table of {num}")
for i in range(1, 11):
    st.write(f"{num} × {i} = {num * i}")
st.header("Python code")
st.code('''
import streamlit as st
st.title("Multiplication Table Generator")
num = st.slider("Select a Number", 1, 20, 5)
st.subheader(f"Table of {num}")
for i in range(1, 11):
    st.write(f"{num} × {i} = {num * i}")''')
