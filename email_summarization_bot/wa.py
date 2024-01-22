
#### coding the user interface as a web app using streamlit

import pandas as pd
import streamlit as st

import connect_extract
import summary 
from calendar_event_creator import CalendarEventCreator

st.header('Email Summarizer')
st.subheader('Teamname - Breadcrumbs')

st.write("EVer haad so many emails that even opening them seemed a dauting task? Fret not,")
st.write("here's a simple interface to summarize your mails for you")
st.write("Follow the steps:")
st.write("1. choose your account")
st.write("2. choose a sender")
st.write("3. choose a time range")
st.write("4. press enter and voila!")

user_input = st.sidebar.selectbox("email ID", ["hftest74@gmail.com"])
password = st.sidebar.text_input("password", type="password")


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

credentials_path = 'credentials.json'
email_text = """
                Hello team,

                Our monthly project meeting is scheduled for January 25th at 2:00 PM. 
                We will be discussing the upcoming conference and other important matters.

                Best regards,
                John Doe
            """

calendar_creator = CalendarEventCreator(credentials_path)
# Add an event
if st.button("Add Event"):
    calendar_creator.add_event(email_text)
# List all events
if st.button("List All Events"):
    calendar_creator.list_events()
# Delete all events
if st.button("Delete All Events"):
    calendar_creator.delete_all_events()