
## code to extract mail from particular user and display it


# Importing libraries
import imaplib
import email

import yaml  #To load saved login credentials from a yaml file

with open("credentials.yml") as f:
    content = f.read()
    
# from credentials.yml import user name and password
my_credentials = yaml.load(content, Loader=yaml.FullLoader)

#Load the user name and passwd from yaml file
user, password = my_credentials["user"], my_credentials["password"]
imap_url = 'imap.gmail.com'
my_mail = imaplib.IMAP4_SSL(imap_url)
my_mail.login(user, password)

# Select the Inbox to fetch messages
my_mail.select('Inbox')

#Define Key and Value for email search

key = 'FROM'
value = 'lachusn212@gmail.com'
_, data = my_mail.search(None, key, value)  #Search for emails with specific key and value

mail_id_list = data[0].split()  #IDs of all emails that we want to fetch 

msgs = [] 
#Iterate through messages and extract data into the msgs list
for num in mail_id_list:
    typ, data = my_mail.fetch(num, '(RFC822)') #RFC822 returns whole message (BODY fetches just body)
    msgs.append(data)

#Now we have all messages, but with a lot of details
#Let us extract the right text and print on the screen

for msg in msgs[::-1]:
    for response_part in msg:
        if type(response_part) is tuple:
            my_msg=email.message_from_bytes((response_part[1]))
            print("_________________________________________")
            print("date:",my_msg['date'])
            print ("subj:", my_msg['subject'])
            print ("from:", my_msg['from'])
            print ("body:")
            for part in my_msg.walk():  
                print(part.get_content_type())
                if part.get_content_type() == 'text/plain':
                   print ("Content ",part.get_payload())



                   
