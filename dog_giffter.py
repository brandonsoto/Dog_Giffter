#!/usr/bin/env python

import urllib
import json
import sys
import argparse

parser = argparse.ArgumentParser(prog='Dog Giffter', description="A Reddit bot that shares cute dog gifs with Redditors that need it most.")
parser.add_argument('-g', '--giphy', metavar="KEY", type=str, required=True, help="the GIPHY API key")
args = parser.parse_args()

def main():
    data=json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=cute+dog&api_key=" + args.giphy + "&limit=25").read())
    print json.dumps(data, sort_keys=True, indent=4)

if __name__ == '__main__':
    print 'Starting app...'
    main()
    print 'Done!'
