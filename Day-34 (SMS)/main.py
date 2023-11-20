from twilio.rest import Client

account_sid = 'AC125ef8a4d23928f3ba8272dd134e7820'
auth_token = '6ce89e2f0c701732cc6fc6ec23e9e1f7'
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello, It's Prajwal here.",
  from_='+12512410520',
  to='+918310260149'
)

print(message.sid)