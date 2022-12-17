import pandas as pd
import streamlit as st
import summary 

st.title("Breadcrumbs!")

st.write("Email Summarizer")

user_input = st.selectbox("Email ID",['josesjoel126@gmail.com','Sandra Skaria <sandra10skaria@gmail.com>','shruthipraveen801@gmail.com','Google <no-reply@accounts.google.com>'])
from_date = st.text_input("From(yyyy-mm-dd):")
to_date = st.text_input("To(yyyy-dd-mm):")

p3 = summary.Table()
p3.Preprocessing()
p3.Data(user_input)
p3.Timeframe(from_date, to_date)
p3.Stopwords()
p3.Plot()