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
import streamlit as st
st.title("reverse a number")
p=(st.text_input("enter a number"))
if st.button("reverse"):
    rev=0
    while p:
        rev=rev*10+p%10
        p//=10
    st.success(f"reverse={rev}")
st.subheader("Python code")
st.code('''
import streamlit as st
st.title("reverse a number")
p=(st.text_input("enter a number"))
if st.button("reverse"):
    rev=0
    while p:
        rev=rev*10+p%10
        p//=10
    st.success(f"reverse={rev}")''')




