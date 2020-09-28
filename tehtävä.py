import json

def load_events():
    with open('events.json') as file
    json_str = file.read()
    return json.loads(json_str)
 