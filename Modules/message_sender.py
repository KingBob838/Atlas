import requests

def send_message(ChannelID, Message, Token):
    headers = {
        "Authorization": Token,
        "Content-Type": "application/json"
    }

    payload = {
        "content": Message
    }

    response = requests.post(f"https://discord.com/api/v9/channels/{ChannelID}/messages", headers=headers, json=payload)

    return response