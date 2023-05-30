from twilio.rest import Client

account_sid = 'AC089b2e953b27ca68060de44a7c026d93'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+13157401145',
  body='Hej {room_id}. Husk din vasketid DDHH. ',
  to='+45XXXXXXXX'
)

print(message.sid)
