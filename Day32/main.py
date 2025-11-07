# Email sender - Google SMTP (Simple mail transfer protocol)
# Mail servers sending through servers and internet 

# hotmail - smtp.live.com
# yahoo - smtp.mail.yahoo.com

import smtplib

myemail = 'bkparthsoni@gmail.com'    # identity_of_my_email_acc@identity_of_my_email_provider 
password='uvsaxwzdwqgohzwc'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()    # transport layer security - Message will be encrypted
    connection.login(user=myemail, password=password)
    connection.sendmail(
        from_addr=myemail, 
        to_addrs='parthsoniofficial18@gmail.com', 
        msg='Subject:Hello\n\nThis is the body of my email'
        )

















































