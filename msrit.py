import streamlit as st
import hashlib

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if the user exists in the database (dummy function here for illustration)
def check_user(username, password):
    # This should connect to your actual database to verify login
    # Here, it simply checks if the hashed password matches a hardcoded value for illustration
    dummy_user = {"username": "student123", "password": hash_password("password123")}
    return username == dummy_user["username"] and hash_password(password) == dummy_user["password"]

# Main app function
def main():
    st.title("MSRIT Annual Day Program - Student Portal")

    # Tabs for Login and Registration
    option = st.sidebar.radio("Select an option:", ("Login", "Register"))

    if option == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if check_user(username, password):
                st.success(f"Welcome, {username}!")
                st.write("ggs")
            else:
                st.error("Invalid username or password")

    elif option == "Register":
        st.subheader("New User Registration")
        roll_no = st.text_input("Roll Number")
        name = st.text_input("Name")
        department = st.selectbox("Department", ["CSE", "ECE", "ME", "CE", "EEE", "Others"])
        phone = st.text_input("Phone Number")
        email = st.text_input("Email")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        if st.button("Register"):
            if password != confirm_password:
                st.error("Passwords do not match")
            else:
                hashed_password = hash_password(password)
                # Store data into the database here
                st.success("Registration successful! You can now login with your credentials.")

if __name__ == "__main__":
    main()
