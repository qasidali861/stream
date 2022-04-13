import streamlit as st
import requests
import json

def fun(title, body):
    headers = {
    'content-type': 'application/json',
    'x-api-key': 'c9ggPwt7vq3mCt07nrMui7e79tDtOoa79sJZDfs8'
    }
    data = {
    "title" : title,
    "body"  : body
    }
    data = json.dumps(data)
    response = requests.post('https://ec2-54-169-194-77.ap-southeast-1.compute.amazonaws.com/categorisation', headers=headers, data=data, verify=False)
    return response



st.title("Neural Lab Internal Categorization Testing API")

m_form = st.form(key = 'form1')

title = m_form.text_input("Enter the Title of Article")

body = m_form.text_area("Enter the Body of Article")

submit = m_form.form_submit_button(label = "Get Categories")

if submit:
    if title == "" and body == "":
        st.subheader("Title and Body is missing. \nPlease Enter the Title & Body!!!!")
    elif body == "":
        st.subheader("Body is missing. \nPlease Enter the Body!!!!")
    elif  title == "":
        st.subheader("Title is missing, \nPlease Enter the Title!!!!")
    else:
        a = fun(title, body)
        a = a.json()
        st.subheader("Time Stamp \n {}".format(a['timeStamp']))
        st.subheader("Article Title \n {}".format(a['title']))
        st.subheader("Top 3 Predicted Categories \n{}".format(a['categorisation']))