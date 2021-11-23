A simple discrord bot for interacting with messages in discord on different servers in different channels.

In config file you should specify:
- `token` (press Ctrl+Shift+I, move to the Network tab and find 'authorization' in Reauest Headers chapter)
- `payload = {
    'op': 2,
    'd': {
        'token': token,
        'properties': {
            '$os': 'linux',
            '$browser': 'chrome',
            '$device': 'pc'
        }
    }
}`


