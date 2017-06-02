from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC1567477569a33786a8869bb66becc75c"
# Your Auth Token from twilio.com/console
auth_token  = "dd2ffc0d2b9e6ce35237412c3a72a737"

client = rest.Client(account_sid,auth_token)

message = client.messages.create(
    to="+12345678901", #Accepts your phone number
    from_="+12345678901", #Accepts Twilio phone number
    body="Hello Krishnan! We are testing using Python. :-)") #Custom text message to be sent.

print(message.sid)