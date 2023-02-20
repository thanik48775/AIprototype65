import requests
import json

if __name__ == "__main__":

    url = 'http://127.0.0.1:5005/home2'
    myobj = {'First': 'Hi!!'}

    x = requests.post(url, data = json.dumps(myobj))

    print(x.text)