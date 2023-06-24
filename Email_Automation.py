import smtplib
# import the smtplib library

to = input("Enter the email address of the receiver : ")

message = input("Enter the message : ")

def sendEmail(to,message):
    # Send the message via local SMTP server.
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    # Login credentials
    server.login('sender-Email','password')
    server.sendmail('sender-Email',to,message)
    server.close()

sendEmail(to,message)
