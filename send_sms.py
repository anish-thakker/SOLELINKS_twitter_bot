from twilio.rest import Client

account_sid = "AC7462e15d3dc7de55f35fa1971f32ce5b"
auth_token  = "f4bbe4412129a90edf1fb09a0279a2d9"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12404447747",
    from_="+12029156653",
    body="Hello from Python!")

print(message.sid)
