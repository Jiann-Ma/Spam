import requests, ssl
from math import floor
import time
import smtplib as smtp
from email.message import EmailMessage

book_url = "http://www.gutenberg.org/files/1342/1342-0.txt"
r = requests.get(book_url)

book_data = r.text.encode("ascii", "ignore").decode("ascii")
word_list = book_data.split(" ")
msg_size = floor(len(word_list) / 1000)
final_msg_size = len(word_list) - (msg_size * 999)

print("Words per message: ", msg_size)
print("\nFinal message size: ", final_msg_size)

a = input("Shall we spam for fun ? \n 1. Sure ! Why not ? \n 2. Maybe next time \n Your input is: ")
userinput = int(a)
if (userinput == 1):
    print("\nInitiating....") 
          
elif (userinput == 2):
    print("\nSee you next time :)") 
else: 
    raise Exception("Enter correct input") 

user = "jiannterngma@gapp.nthu.edu.tw"
password = "s828230604"
fr_address = "jiannterngma@gapp.nthu.edu.tw"
to_address = "paprikaNoharm@gmail.com"    #"alisachiu@gmail.com"
smtp_host = "smtp.gmail.com"
smtp_port = 465

context=ssl.create_default_context()

subject = "A surprise from your the sincerest friend, present you \"Pride and Prejudice\", by Jane Austen"
msg_text = ""
start_pos = 0
msg_count = 0

for b in range(20):
    smtpObj = smtp.SMTP_SSL(host=smtp_host, port=smtp_port)
    #smtpObj.connect("smtp.gmail.com",587)
    #smtpObj.ehlo()
    #smtpObj.starttls
    smtpObj.login(user=user, password=password)

    for i in range(50):
        if msg_count == 1000:
            start_pos = (len(word_list)-final_msg_size)
            msg_text = " ".join(word_list[start_pos:start_pos + msg_size])
        else:
            start_pos = msg_count * msg_size
            msg_text = " ".join(word_list[start_pos:start_pos + msg_size])
        msg = EmailMessage()
        msg["From"] = fr_address
        msg["To"] = to_address
        msg["Subject"] = subject + str(msg_count+1)
        msg.set_payload(msg_text)

        msg_count += 1

        smtpObj.send_message(msg)
        time.sleep(0.5)

    time.sleep(60)

    smtpObj.close()
print("Mission completed.")


