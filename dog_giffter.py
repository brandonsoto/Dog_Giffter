#!/usr/bin/env python

import urllib.request
import json
import yaml

credentials = yaml.load(open("credentials.yml", 'r'))

def main():
    data=json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q=cute+dog&api_key=" + credentials["giphy"]["key"] + "&limit=25").read())
    print(json.dumps(data, sort_keys=True, indent=4))

if __name__ == '__main__':
    print('Starting app...')
    main()
    print('Done!')
