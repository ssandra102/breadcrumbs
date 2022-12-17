from tabulate import tabulate
from IPython.display import display
import pandas as pd
from datetime import datetime
import re
import streamlit as st
class Table:
    
    def Preprocessing(self):
        
        global df4
        global df3

        df = pd.read_csv('Mails.csv')
        df3 = df.assign(From = df['From'].str.split(';')).explode('From').reset_index(drop = True)
        df3.rename(columns = {'From':'Sender'}, inplace = True)
        date = []

        for i in range(len(df3)):
        # Parse the RFC 2822 time string
            if (df3.loc[i,"Timestamp"]) is not None:
                time_string = df3.loc[i,"Timestamp"]
                time_string = re.sub("GMT","+0000",time_string)
                time = datetime.strptime(time_string, "%a, %d %b %Y %H:%M:%S %z")

        # Convert the time to the desired format
                formatted_time = time.strftime("%Y-%m-%d")
                date.append(formatted_time)
        df4=df3.drop(['Timestamp'], axis = 1)
        df4['Date'] = date
        print(df4)        

    def Data(self,user_input):

        global valid_email
        global words
        
        email_id = df4['Sender'] == user_input
        df5 = df4.where(email_id).dropna()

        valid_email = df4.isin([user_input]).any().any()
        if valid_email:
            words = df5.drop(['Sender'], axis = 1)
            print(words)
        else:
            print('\n Enter valid email id and try again!')

    def Timeframe(self,from_date,to_date):

        global df6

        if valid_email:
            filtered_df = words.loc[(words['Date'] >= from_date) & (words['Date'] <= to_date)]
            df6 = pd.DataFrame(filtered_df)
        else:
            pass

    def Stopwords(self):

        global df7

        if valid_email:
            df7 = df6.drop(['Date'], axis = 1)
            stop_words = ["Accepted:","Cancelled:","Re:","Fw:","RE:","FW:","Fwd:","Recurring"]

            df7 = df7["Subject"].apply(lambda keys: ' '.join(key for key in keys.split() if key not in stop_words))
        else:
            pass

    def Plot(self):

        if valid_email:

            df8 = pd.DataFrame(df7)
            df8 = df8['Subject'].value_counts()
            df8.astype(str)
            final_dataframe = pd.DataFrame(df8)
            head = ["Subject","Frequency"]
            print(tabulate(final_dataframe, headers = head, tablefmt="fancy_grid"))
            final_dataframe.to_csv('end.csv')
            df = pd.read_csv("end.csv", names=['Subject','Frequency'])
            st.table(df[1:])
        else:
            pass
