from tabulate import tabulate
from IPython.display import display
import pandas as pd
class Table:
    
    def Preprocessing(self):
        
        global df4
        global df3

        df = pd.read_excel('mailsSend.xlsx')
        df1 = df.assign(To = df['To'].str.split(';')).explode('To').reset_index(drop = True)
        df1.rename(columns = {'To':'Recipient'}, inplace = True)
        df2 = pd.read_excel('mailsReceived.xlsx')
        df2.rename(columns = {'From':'Recipient'}, inplace = True)
        Merged = [df1,df2]
        df3 = pd.concat(Merged).reset_index(drop=True)
        print(df3)
        date = df3['Timestamp'].str.split( 'T', expand=True)
        print(date)
        date.drop(date.columns[1], axis = 1 , inplace=True)
        print(date)
        df4 = df3.assign(Date = date)
        print(df4)
        df4.drop(['Timestamp'], axis = 1)

    def Data(self):

        global valid_email
        global words
        

        user_input = input("Email Id: ")
        email_id = df4['Recipient'] == user_input
        df5 = df4.where(email_id).dropna()
        print(df5)

        valid_email = df4.isin([user_input]).any().any()
        if valid_email:
            words = df5.drop(['Recipient','Timestamp'], axis = 1)
            print(words)
        else:
            print('\n Enter valid email id and try again!')

    def Timeframe(self):

        global df6

        if valid_email:

            from_date = input("From:\n(year-month-date) ")

            to_date = input("To:\n(year-month-date) ")

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
        else:
            pass
    
p3 = Table()
p3.Preprocessing()
p3.Data()
p3.Timeframe()
p3.Stopwords()
p3.Plot()
