import os, random, datetime as dt, smtplib, pandas

today = dt.datetime.now()
month = today.month
day = today.day
today_date = (day, month)
print(today_date)

def random_letter(recipient_name):
    files = [f for f in os.listdir(r'Day32\letter_templates')]
    print(random.choice(files))
    with open(f'Day32/letter_templates/{random.choice(files)}') as f:
        content = f.read()
        letter = content.replace('[NAME]', recipient_name)    # returns a new string 
        return letter

random_letter('Parth')


myemail = 'bkparthsoni@gmail.com'  
password='uvsaxwzdwqgohzwc' 

def send_mail(recipient_email, letter):
    with smtplib.SMTP('smtp.gmail.com') as connection: 
        connection.starttls()                   
        connection.login(myemail, password)
        connection.sendmail(from_addr=myemail, to_addrs=recipient_email,
                            msg=f"Subject: A very happy birthday\n\n{letter}")


with open(r'Day32\birthdays.csv') as bdates:
    df = pandas.read_csv(bdates)

    print(df)
    print(len(df))
    b_day, b_month = list(df['day']), list(df['month'])
    b_date = [(b_day[i], b_month[i]) for i in range(len(df))]  #list of tuples

    print(b_date)

    if today_date in b_date:
        rows_check1 = df[df['day'] == today_date[0]]  
        final_row = rows_check1[rows_check1['month'] == today_date[1]]
        
        recipient_name = final_row['name'].iloc[0]
        recipient_email = final_row['email'].iloc[0]

        # print(recipient_name)
        # print(recipient_email)

        letter_to_send = random_letter(recipient_name)
        send_mail(recipient_email, letter_to_send)  


# This program can be automated for daily run at cloud using platforms like pythonanywhere