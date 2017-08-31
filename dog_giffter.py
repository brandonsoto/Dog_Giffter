#!/usr/bin/env python

import requests
import json
import yaml

credentials = yaml.load(open("credentials.yml", 'r'))
giphy = credentials["giphy"]["key"]
reddit = credentials["reddit"]

def main():
    data = requests.get("http://api.giphy.com/v1/gifs/search?q=cute+dog&api_key=" + giphy +
            "&limit=25").json()
    print(json.dumps(data, sort_keys=True, indent=4))

if __name__ == '__main__':
    print('Starting app...')
    print('giphy key: ' + giphy)
    print('reddit: ' + str(reddit))
    main()
    print('Done!')
