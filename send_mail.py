import smtplib

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('lprr1003@gmail.com','ethrtjrqsbjgwhsm')
    server.sendmail('lprr1003@gmail.com',to,content)
    server.close()