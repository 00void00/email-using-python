>>> from email.message import EmailMessage
>>> message = EmailMessage()
>>> sender = "say@gmail.com"
>>> receiver = "you@gmail.com"
>>> message['From'] = sender
>>> message['To'] = receiver
>>> message['Subject'] = 'Greetings from {} to {}!'.format(sender, receiver)
>>> body = """Hey there!
... ...
... ... I'm learning to send emails using Python!"""
>>> message.set_content(body)
>>> print(message)


#From, To, and Subject are examples of email header fields
