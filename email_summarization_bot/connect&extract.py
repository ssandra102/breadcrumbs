import imaplib
import email
import csv

import yaml  #To load saved login credentials from a yaml file

#Load the user name and passwd from yaml file
user, password = "htest1231@gmail.com", "nzhnkrruvephlnnk"


#URL for IMAP connection
imap_url = 'imap.gmail.com'

# Connection with GMAIL using SSL
my_mail = imaplib.IMAP4_SSL(imap_url)

# Log in using your credentials
my_mail.login(user, password)

# Select the Inbox to fetch messages
my_mail.select('Inbox')

#Define Key and Value for email search
_, data = my_mail.search(None,'ALL')  

mail_id_list = data[0].split()  #IDs of all emails that we want to fetch 

msgs = [] # empty list to capture all messages
#Iterate through messages and extract data into the msgs list
for num in mail_id_list:
    typ, data = my_mail.fetch(num, '(RFC822)') #RFC822 returns whole message (BODY fetches just body)
    msgs.append(data)

k = [['Timestamp', 'Subject','From']]
l = []
for msg in msgs[::-1]:
    for response_part in msg:
        if type(response_part) is tuple:
            l= []
            my_msg=email.message_from_bytes((response_part[1]))
            l.append(my_msg['date'])
            l.append(my_msg['subject'])
            l.append(my_msg['from'])
            k.append(l)
print(k)
with open("Mails.csv",  "w") as csvfile:
    write = csv.writer(csvfile)
    write.writerows(k)

                   