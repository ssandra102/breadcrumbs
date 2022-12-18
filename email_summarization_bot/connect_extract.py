
#### Connecting to gmail and extracting all emails into csv file

import imaplib
import email
import csv
#function to get all mails recieved from a psrticular user

def getAllEmails(username, password):
    # used to make an connection over imap4 server gmail
    my_mail = imaplib.IMAP4_SSL("imap.gmail.com")    
    # login is used to identify client
    my_mail.login(username, password)
    print("Login success..........")
    
    # we can select any directory using mail.list(), in our case we have selected inbox.
    my_mail.select("inbox")
    _, data = my_mail.search(None,'ALL')  #Search for emails with specific key and value
    mail_id_list = data[0].split()  #IDs of all emails that we want to fetch 

    msgs = []
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
                my_msg=email.message_from_bytes((response_part[1]))
                print("_________________________________________")
                print("date:",my_msg['date'])
                print ("subj:", my_msg['subject'])
                print ("from:", my_msg['from'])
    ## writing into csv file
    with open("Mails.csv",  "w") as csvfile:
        write = csv.writer(csvfile)
        write.writerows(k)

                   