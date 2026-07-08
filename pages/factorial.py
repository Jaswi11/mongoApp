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
st.title("Factorial python code")
n=st.slider("Pick a number",1,100)
f=1
for i in range(1,n+1):
    f=f*i
st.success(f"factorial of {n} is {f}")
st.subheader("Python code")
with st.expander("See The Python Code"):
    st.code('''
    import streamlit as st
    st.title("Factorial python code")
    n=st.slider("Pick a number",1,100)
    f=1
    for i in range(1+n+1):
    f=f*i
    st.success(f"factorial of {n} is {f}")''')
