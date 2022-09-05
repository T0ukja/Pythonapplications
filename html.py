from pathlib import Path
from redmail import outlook

#Configuring account
outlook.username = 'your email'
outlook.password = 'your password'

# Sending
outlook.send(
    subject="Example email",
    receivers=['email to send'],
       html="""
        <h1>Hi,</h1>
        <p>nice to meet you</p>
        <p>Kind regards
        <br>{{ sender.full_name }}</p>
    """,
)


