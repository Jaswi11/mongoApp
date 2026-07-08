import streamlit as st

st.markdown("""
<style>

/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #BFEAF5, #EAFDFC);
}

/* Title Style */
h1 {
    color: #0A2647;
    text-align: center;
    font-size: 40px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #144272;
}

/* Button Styling */
.stButton > button {
    background-color: #144272;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 8px 20px;
    transition: 0.3s;
}



/* Card Style */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

st.title("🐍 ALL BASIC PYTHON CODE")
st.markdown('<p class="subtitle">Learn Python in a Smart & Easy Way 🚀</p>', unsafe_allow_html=True)

st.image("https://www.python.org/static/community_logos/python-logo.png", width=250)

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["📘 Basics", "⚙️ Conditions", "🔁 Loops", "👤 Account"])

# ----------- TAB 1: BASICS -----------
with tab1:
    st.subheader("📘 Basic Programs")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">🔢 Factorial<br><br></div>', unsafe_allow_html=True)
        if st.button("Run Factorial"):
            num = st.number_input("Enter number", key="fact")
            if st.button("Calculate"):
                fact = 1
                for i in range(1, num+1):
                    fact *= i
                st.success(f"Factorial = {fact}")

    with col2:
        st.markdown('<div class="card">🔁 Reverse Number<br><br></div>', unsafe_allow_html=True)
        if st.button("Run Reverse"):
            num = st.text_input("Enter number", key="rev")
            if st.button("Reverse Now"):
                st.success(f"Reverse = {num[::-1]}")

# ----------- TAB 2: CONDITIONS -----------
with tab2:
    st.subheader("⚙️ Condition Programs")

    num = st.number_input("Enter a number")

    if st.button("Check Even/Odd"):
        if num % 2 == 0:
            st.success("Even Number")
        else:
            st.error("Odd Number")

# ----------- TAB 3: LOOPS -----------
with tab3:
    st.subheader("🔁 Loop Programs")

    num = st.number_input("Enter number for table", key="table")

    if st.button("Generate Table"):
        for i in range(1, 11):
            st.write(f"{num} x {i} = {num*i}")

# ----------- TAB 4: ACCOUNT -----------
with tab4:
    st.subheader("👤 Account Section")

    option = st.selectbox("Choose", ["Signin", "Signup"])

    if option == "Signin":
        st.text_input("Username")
        st.text_input("Password", type="password")
        st.button("Login")

    else:
        st.text_input("Create Username")
        st.text_input("Create Password", type="password")
        st.button("Signup")





