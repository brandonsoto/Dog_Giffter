#!/usr/bin/env python

import json
import praw
import requests
import yaml

credentials = yaml.load(open("credentials.yml", 'r'))
gc = credentials["giphy"]["key"]  # giphy credentials
rc = credentials["reddit"]  # reddit credentials


# Performs analysis on a given comment
def analyze_comment(comment):
    # TODO: perform sentiment analysis on comment body here
    print('################################################ START')
    print(comment.body)
    print('################################################ END\n')
    # if in sentiment range
    #     reply_to(comment)
    pass


# replies to the given comment with a cute dog gif
def reply_to(comment):
    # TODO: need to select picture and format reply text
    dog_pictures = requests.get("http://api.giphy.com/v1/gifs/search?q=cute+dog&api_key=" + gc + "&limit=25").json()
    print(json.dumps(dog_pictures, sort_keys=True, indent=4))
    comment.reply("reply text goes here")


def main():
    # reddit instance
    r = praw.Reddit(client_id=rc['client_id'], client_secret=rc['client_secret'], user_agent=rc['user_agent'],
                    username=rc['username'], password=rc['password'])

    popular = r.subreddit('popular').controversial(limit=1)  # TODO: change limit when sentiment analysis is complete

    for submission in popular:
        submission.comments.replace_more(limit=0)  # remove MoreComments instances
        print("---------------------------------------------------------------------")
        print("title=", submission.title, ", id=", submission.id, ", url=", submission.url)
        for comment in submission.comments.list():
            analyze_comment(comment)
        print("---------------------------------------------------------------------")


if __name__ == '__main__':
    print('Starting app...')
    print('giphy key: ' + gc)
    print('reddit: ' + str(rc))
    main()
    print('Done!')
