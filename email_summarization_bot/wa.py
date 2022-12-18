
#### coding the user interface as a web app using streamlit

import pandas as pd
import streamlit as st

import connect_extract
import summary 

st.header('Email Summarizer')
st.subheader('Teamname - Breadcrumbs')

st.write("EVer haad so many emails that even opening them seemed a dauting task? Fret not,")
st.write("here's a simple interface to summarize your mails for you")
st.write("Follow the steps:")
st.write("1. choose your account")
st.write("2. choose a sender")
st.write("3. choose a time range")
st.write("4. press enter and voila!")
user_input = st.sidebar.selectbox("email ID", ["htest1231@gmail.com"])
password = st.sidebar.text_input("password", type="password")#nzhnkrruvephlnnk
connect_extract.getAllEmails(user_input,password)

df = pd.read_csv("Mails.csv")
st.dataframe(df)

user_input = st.selectbox("email ID",["AARSHA LEENA <malu22leena@gmail.com>","Lakshmi S Nair <lachusn212@gmail.com>","Sandra Skaria <sandra10skaria@gmail.com>","Shruthi Praveen <shruthipraveen801@gmail.com>"])
from_date = st.text_input("from")
to_date = st.text_input("to")

p3 = summary.Table()
p3.Preprocessing()
p3.Data(user_input)
p3.Timeframe(from_date, to_date)
p3.Stopwords()
p3.Plot()

