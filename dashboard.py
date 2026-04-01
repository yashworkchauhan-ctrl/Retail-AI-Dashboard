from database import create_usertable
create_usertable()
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Retail AI Dashboard", layout="wide")

# ---------------- DATABASE ----------------

conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)")
    conn.commit()

def add_user(username,password):
    c.execute("INSERT INTO users(username,password) VALUES (?,?)",(username,password))
    conn.commit()

def login_user(username,password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    return c.fetchall()

create_table()

# ---------------- SESSION ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------

def login_page():

    menu = ["Login","Sign Up"]
    choice = st.sidebar.selectbox("Menu",menu,key="menu_select")

    if choice == "Login":

        st.title("Login")

        username = st.text_input("Username",key="login_user")
        password = st.text_input("Password",type="password",key="login_pass")

        if st.button("Login",key="login_btn"):

            result = login_user(username,password)

            if result:
                st.session_state.logged_in = True
                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Wrong Username or Password")

    if choice == "Sign Up":

        st.title("Create Account")

        new_user = st.text_input("Username",key="signup_user")
        new_pass = st.text_input("Password",type="password",key="signup_pass")

        if st.button("Signup",key="signup_btn"):

            add_user(new_user,new_pass)

            st.success("Account Created Successfully")
            st.info("Go to Login")


# ---------------- DASHBOARD ----------------

def dashboard():

    st.title("Retail AI Dashboard")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Go to",
        ["Overview","Product Analysis","Profit Analysis"]
    )

    file = st.file_uploader("Upload CSV Dataset",type=["csv"])

    if file is not None:

        df = pd.read_csv(file)

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        if page == "Overview":
            st.write(df.describe())

        if page == "Product Analysis":

            if "Category" in df.columns and "Sales" in df.columns:

                fig = px.bar(df,x="Category",y="Sales",color="Category")

                st.plotly_chart(fig,use_container_width=True)

            else:
                st.warning("Dataset must contain Category and Sales columns")

        if page == "Profit Analysis":

            if "Category" in df.columns and "Profit" in df.columns:

                fig = px.bar(df,x="Category",y="Profit",color="Category")

                st.plotly_chart(fig,use_container_width=True)

            else:
                st.warning("Dataset must contain Category and Profit columns")


# ---------------- APP ----------------

if st.session_state.logged_in:

    dashboard()

else:

    login_page()
