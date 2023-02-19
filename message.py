from twilio.rest import Client


class Message():
    def __init__(self, account_sid, auth_token):
        self.account_sid = account_sid
        self.auth_token = auth_token
        
    def create_message(self, message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(body=f"{message}", from_="+17082496763", to="+447437592308")
        return message