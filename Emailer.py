# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:12:31 2021

@author: phjlj
"""

"""imports"""
import sys
import smtplib
from datetime import datetime 

#function: banner
def banner():    
    sys.stdout.write("""
                               .,,uod8B8bou,,.
                  ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
             ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
             !...:!TVBBBRPFT||||||||||!!^^""'   ||||
             !.......:!?|||||!!^^""'            ||||
             !.........||||                     ||||
             !.........||||  pogger             ||||
             !.........||||                     ||||
             !.........||||                     ||||
             !.........||||                     ||||
             !.........||||                     ||||
             `.........||||                    ,||||
              .;.......||||               _.-!!|||||
       .,uodWBBBBb.....||||       _.-!!|||||||||!:'
    !YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
    !..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
    !....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
    !......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
    !........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
    `..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
      `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
        `........::::::::::::::::;iof688888888888888888888b.     `
          `......:::::::::;iof688888888888888888888888888888b.
            `....:::;iof688888888888888888888888888888888899fT!
              `..::!8888888888888888888888888888888899fT|!^"'
                `' !!988888888888888888888888899fT|!^"'
                    `!!8888888888888888899fT|!^"'
                      `!988888888899fT|!^"'
                        `!9899fT|!^"'
                          `!^"'
    
""")
    print("send Emails via Python")

#class: sendEmail -> send emails with script
class sendEmail:
    
    #instance variables
    def __init__(self):
        self.reciever = str(input("enter the reciever address: "))
        self.sender = str(input("enter your email address: "))
        self.password = str(input("enter your email password: "))
        self.server = int(input("enter the mailing server [1=gmail, 2=yahoo, 3=outlook]: "))
        #set the server
        if (self.server == 1): 
            self.server = "smtp.gmail.com"
        elif (self.server == 2): 
            self.server = "smtp.mail.yahoo.com"
        elif (self.server == 3): 
            self.server = "smtp-mail.outlook.com"
    #method: construct email
    def construct_email(self):
        subject = str(input("enter the subject: "))
        message = str(input("enter the message: "))
        self.email = '''From: %s\nTo: %s\nSubject %s\n%s\n''' % (self.sender, self.reciever, subject, message)
    #method: send
    def send(self):
        try:
            sender = smtplib.SMTP(self.server, 587)
            sender.ehlo()
            sender.starttls()
            sender.ehlo()
            sender.login(self.sender, self.password)
            sender.sendmail(self.sender, self.reciever, self.email)
        except Exception as ERR:
            return ERR
        
#class: repeater
class repeater(sendEmail):
    def repetitive_send(self):
        count = int(input("enter amount of emails: "))
        for instance in count:
            try:
                sender = smtplib.SMTP(self.server, 587)
                sender.ehlo()
                sender.starttls()
                sender.ehlo()
                sender.login(self.sender, self.password)
                sender.sendmail(self.sender, self.reciever, self.email)
            except Exception as ERR:
                return ERR

if __name__ == "__main__":
    banner()
    mode = str(input("enter mode [single or repeater]: "))
    if mode == "single":
        sys.stdout.write("single mode")
        AUTO = sendEmail()
        AUTO.construct_email()
        AUTO.send()
    elif mode == "repeater":
        sys.stdout.write("repeater mode")
        AUTO = repeater()
        AUTO.construct_email()
        AUTO.repetitive_send()
    else:
        pass




































