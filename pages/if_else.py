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



st.title("wap on python to find greatest btw two number using if else statement")
t1=st.text_input("enter 1st number")
t2=st.text_input("enter 2nd number")
if st.button("GREATER"):
    if t1>t2:
        st.success(f"greater number={t1}")
    else:
        st.success(f"greater number={t2}")

