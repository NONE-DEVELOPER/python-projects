import smtplib


to = input("Enter the email address of the receiver : ")

message = input("Enter the message : ")

def sendEmail(to,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('sender-Email','password')
    #Here enter the gmail and password of the sender with in the single quotes 
    server.sendmail('sender-Email',to,message)
    server.close()

sendEmail(to,message)
