import requests

from config import token


def send(message: str, channel_id: str) -> None:
    """send message to the channel_id"""
    headers = {
        'authorization': token
    }

    payload = {
        'content': message
    }
    requests.put(
        f'https://discord.com/api/v9/channels/{channel_id}/messages',
        data=payload, headers=headers
    )


def main():
    channel_id: str = '1234567890'
    send('Hello, World', channel_id)


if __name__ == '__main__':
    main()
