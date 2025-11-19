# Email sender - Google SMTP (Simple mail transfer protocol)
# Mail servers sending through servers and internet 

# hotmail - smtp.live.com
# yahoo - smtp.mail.yahoo.com

import smtplib
import random 
import datetime as dt

myemail = 'bkparthsoni@gmail.com'    # identity_of_my_email_acc@identity_of_my_email_provider 
password='uvsaxwzdwqgohzwc'         #your Gmail password (or an App Password if you have 2FA enabled).

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()    # transport layer security - Message will be encrypted
#     connection.login(user=myemail, password=password)  
#     connection.sendmail(
#         from_addr=myemail, 
#         to_addrs='parthsoniofficial18@gmail.com', 
#         msg='Subject:Hello\n\nThis is the body of my email'
#         )

def send_quote(quote):
    with smtplib.SMTP('smtp.gmail.com') as connection:    #connection to SMTP server | 'smtp.gmail.com' is Gmail's SMTP server address.
        connection.starttls()                   #TLS (Transport Layer Security) encrypts the connection, making it secure.
        connection.login(myemail, password)
        connection.sendmail(from_addr=myemail, to_addrs=myemail,
                            msg=f"Subject: Tuesday Motivation\n\n{quote}")


now = dt.datetime.now()
if now.weekday() == 1:
    with open(r'Day32\quotes.txt') as quotes_file:
        quote_list = quotes_file.readlines()
        quote = random.choice(quote_list)
        
        print(quote)
        send_quote(quote=quote)














































