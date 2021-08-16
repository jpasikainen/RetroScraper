import json
import os
import requests
from haralyzer import HarParser, HarPage

# Download the .har file from Developer tools and put it to the same folder
# with this script
with open('play.retro-mmo.com.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

data = har_parser.har_data["entries"]

for entry in data:
    if entry["response"]["content"]["mimeType"].find("image/") == 0:
        url = entry["request"]["url"]
        res = requests.get(url)
        if res.ok:
            filename = url.split("https://play.retro-mmo.com/res/")[1]
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            print(filename)
            with open(filename, "wb") as f:
                f.write(res.content)