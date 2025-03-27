import smtplib

to = input("Enter the Email of Recipent: \n")

content = input("Enter the Content for Mail: \n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("senderemail@gmail.com", '1234')
    server.sendmail("senderemail@gmail.com", to, content)
    server.close()

sendEmail(to, content)