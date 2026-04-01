import streamlit as st
from database import create_usertable,add_userdata,login_user

def login_page():

    create_usertable()

    menu = ["Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Login":

        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password",type='password')

        if st.button("Login"):

            result = login_user(username,password)

            if result:
                st.session_state.logged_in = True
                st.success("Logged In Successfully")
                st.rerun()
            else:
                st.error("Incorrect Username/Password")

    else:

        st.subheader("Create New Account")

        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')

        if st.button("Signup"):
            add_userdata(new_user,new_password)
            st.success("Account Created Successfully")
