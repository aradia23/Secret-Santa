import random
import smtplib
import os

# Simple function to login and send emails from my email stored in enviroment variables
def sendMail (toEmail, santa, r):
    password = os.environ.get("EMAIL_PASS")
    sender = os.environ.get("EMAIL")
    to_email = toEmail
    subject = f'Secret Santa'
    text = """ 
    Hi %s, 

    You are giving a present to %s. 

    Kind regards, 

    Secret Santa Python """ %(santa, r)
    message = 'Subject: {} \n\n{}'.format(subject, text)
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        try :
            smtp.login(sender, password)
            print ('Successfully Logged into Email Account')
        except:
            print ('Failed to log into Email Account')
        try:
            smtp.sendmail(sender, to_email, message)
            print('Email Successfully Sent')
            return True
        except:
            print('Failed to Send Email')
            return False

# Check if email has not already been used and contains an @ sign        
def validateEmail(email, email_List):
    return (email not in email_List and '@' in email)

# Function to assign the santas and to send an email to each santa
def assignSantas (names, emails, reciepiants):
    length = len(names)
    for i in range(length): 
        santa = names[i]
        r = random.choice(reciepiants)
        
        while santa == r: 
            r = random.choice(reciepiants)
        
        reciepiants.remove(r)
        
        bol = sendMail(emails[i], santa, r)
    return bol

def main ():
    santaNames = []
    santasEmails = []
    
    numOfParticpants = int(input('Enter the number of Participants \n'))

    for i in range (1, (numOfParticpants + 1)):
        name = input ("Enter name of participant " + str(i) + "\n")
        email = input ("Enter email of participant " + str(i) + "\n")
        
        while validateEmail(email, santasEmails) == False:
            print ('Not valid Email address')
            email = input ("Enter valid email of participant " + str(i) + "\n")
            
        santaNames.append(name)
        santasEmails.append(email)
    
    reciepiants = santaNames.copy()

    assignSantas(santaNames, santasEmails, reciepiants)
    



if __name__ == '__main__': 
    main()








    


