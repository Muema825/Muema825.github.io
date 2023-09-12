import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth


cred = credentials.Certificate('mentalhealthproject-1886a-bcd5abc019c0.json')
firebase_admin.initialize_app(cred)


if st.button('Create my account'):
    user = auth.create_user(name= name, gender=gender, phone=phone , email = email, password= password, uid = username )
    st.success('Account created successfully!')
    st.markdown('Please Login using your email and password')
    st.balloons()


