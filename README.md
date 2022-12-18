# breadcrumbs<br>
There are 3 files<br>
1. connect_extract.py<br>
2. summary.py<br>
3. wa.py<br>

connect_extract.py - This is used to connect to user's gmail and extract all the mails into csv file 'Mails.csv'.<br>
summary.py - Filter all the mails from a specific person, recieved during a specified time period.<br>
wa.py - summarizer is presented as a web app.<br>

## Language used 
python<br>
## Libraries used 
imaplib, email, csv, tabulate, pandas, datetime, re, streamlit.

## Walkthrough
Prerequisites: User must enable imap/pop settings and two step verification in their gmail account. Once this is done, user must generate app password and save it.<br>
Constraint: We consider the subject to be ideal which includes the keywords for our summarization module.<br>
User logs in using gmail id and app password. Once logged in, all emails in the inbox are fetched. Now we can filter the mails based on a particular sender and timespan. The table shows the subjects and frequency of mails based on that particular subject if it is repeated.  
