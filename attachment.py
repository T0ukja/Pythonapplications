from pathlib import Path
from redmail import outlook

#Configuring account
outlook.username = 'your email'
outlook.password = 'your password.'

# Sending
outlook.send(
    subject="Example email",
    receivers=['email to send'],
   # Change attachment if you test it
     attachments={
   'note.png': Path('note.png'),
   'gyro.csv' : Path('charts/gyro.csv')
    },
    text= "Hello, I have attachments included"
)
