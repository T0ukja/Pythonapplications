from redmail import outlook

#Configuring account
outlook.username = 'your email!'
outlook.password = 'your password'

# Sending
outlook.send(
    subject="Example email",
    receivers=['email address to send the post'],
    text="Hi, this is an email from python."
)
