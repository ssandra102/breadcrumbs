# breadcrumbs<br>
There are 3 files<br>
1. connect_extract.py<br>
2. summary.py<br>
3. wa.py<br>
4. calendar_event_creator.py<br>

connect_extract.py - This is used to connect to user's gmail and extract all the mails into csv file 'Mails.csv'.<br>
summary.py - Filter all the mails from a specific person, recieved during a specified time period.<br>
calendar_event_creator.py - Extract the event date and summary mentioned in the email, and add them to the user's google calendar.<br>
wa.py - summarizer is presented as a web app.<br>

## Stacks used 
1. python
2. Streamlit

## Libraries used 
imaplib, email, csv, tabulate, pandas, datetime, re, streamlit, googleapiclient, spacy

## Walkthrough
Prerequisites: User must enable imap/pop settings and two step verification in their gmail account. Once this is done, user must generate app password and save it.<br>
Running the following command in terminal deploys the web app in local host:
```python
      streamlit run wa.py
```
User logs in using gmail id and app password. Once logged in, all emails in the inbox are fetched. Now we can filter the mails based on a particular sender and timespan. The table shows the subjects and frequency of mails based on that particular subject if it is repeated.  
Constraint: 
1. We consider the subject to be ideal which includes the keywords for our summarization module.<br>
2. Deployment cannot be done right now due to encryption issues.

## Screenshots
![screenshots](https://user-images.githubusercontent.com/75726461/208280959-9a0d130e-4a9c-4e1d-a529-d0c6acb2eb25.jpeg)
![screenshot1](https://user-images.githubusercontent.com/75726461/208280947-f97a82ee-708e-4fb4-b288-a4d04437f03b.jpeg)
![screenshot2](https://user-images.githubusercontent.com/75726461/208280951-0f890d04-a73c-4536-bcfe-5c50d4eab3a8.jpeg)

