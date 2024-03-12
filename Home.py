import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def main():
    st.set_page_config(
        page_title="Telecom Churn Rate Application",
        page_icon=":telephone_receiver:",
        layout="wide"
    )
#👋
    st.markdown('# 🏡Welcome to Telecom Churn Rate Application')
    st.write("This app predicts the churn rate of customers in a telecom company .")
    st.markdown("### Enter username == Drop_ins and password == guest000 to use this app")
    st.write('## Features:')
    st.write("- Explore factors contributing to churn rate on **Data**🗃️ page.")
    st.write("- Predict churn rate using machine learning models.🤖")
    st.write("- View historical churn rate data.")

    st.write('## Get Started:')
    st.write("- Navigate to the **Predict**📈 page to make predictions.")
    st.write("- Navigate to the **History** page to view historical churn rate data.")

    st.write("Use the ⬅sidebar to navigate between different pages and to 🔑🔓log in.")

    # To Check if user is logged in
    if 'authentication_status' not in st.session_state:
        st.session_state.authentication_status = False

    if not st.session_state["authentication_status"]:
        st.sidebar.markdown("**Guest Login Credentials**")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        login_button = st.sidebar.button("Login")

        if login_button:
            if username == 'Drop_ins' and password == 'guest000':
                st.session_state["authentication_status"] = True
            else:
                st.warning(" ❌Incorrect username or password. Please try again.")

if __name__ == "__main__":
    main()
