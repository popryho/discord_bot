import json
from threading import Thread
from time import sleep

from websocket import WebSocket

from config import payload
from react import add_reaction


def send_json_request(ws, request):
    ws.send(json.dumps(request))


def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)


def heartbeat(interval, ws):
    while True:
        sleep(interval)
        heartbeat_json = {
            'op': 1,
            'd': 'null'
        }
        send_json_request(ws, heartbeat_json)


def action(event: dict):
    try:
        print(f"{event['d']['author']['username']}: {event['d']['content']}")

        if event['d']['author']['username'] == 'my_username':
            from emoji import emojize
            add_reaction(emoji=emojize(':thumbs_up:'),
                         channel_id=event['d']['channel_id'],
                         message_id=event['d']['id'])
    except (KeyError, TypeError):
        pass


def main():
    ws = WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    event = receive_json_response(ws)

    heartbeat_interval = event['d']['heartbeat_interval'] / 1000

    thread = Thread(target=heartbeat, args=(heartbeat_interval, ws))
    thread.start()

    send_json_request(ws, payload)

    while True:
        event = receive_json_response(ws)
        action(event)


if __name__ == '__main__':
    main()
