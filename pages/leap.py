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

st.title("Leap Year or not")
year = st.slider("Select a Year", 1900, 2100, 2024)
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    st.success(f"{year} is a Leap Year.")
else:
    st.error(f"{year} is Not a Leap Year.")
st.header("Python code")
st.code('''
import streamlit as st
st.title("Leap Year or not")
year = st.slider("Select a Year", 1900, 2100, 2024)
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    st.success(f"{year} is a Leap Year.")
else:
    st.error(f"{year} is Not a Leap Year.")''')
