import time
import json
import requests

f = open("gps-output.nmea", "r")
lines = f.readlines()
line_index = 0

while True:
    line = str.strip(lines[line_index])
    payload = {
        'pet-id': 'Rover',
        'timestamp': int(time.time()),
        'nmea-sentence': line
    }
    r = requests.post("INSERT URI", data = json.dumps(payload))
    print("posted")
    time.sleep(3)
    line_index += 1
    if (line_index == len(lines)):
        line_index = 0
