import requests
from emoji import emojize

from config import token


def add_reaction(emoji: str, channel_id: str, message_id: str) -> None:
    """add reaction emoji to the message_id in channel_id"""
    headers = {
        'authorization': token
    }
    requests.put(
        f'https://discord.com/api/v8/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/%40me',
        headers=headers
    )


def main():
    channel_id: str = '1234567890'
    message_id: str = '1234567890'
    emoji_name: str = ':thumbs_up:'
    add_reaction(emojize(emoji_name), channel_id, message_id)


if __name__ == "__main__":
    main()
