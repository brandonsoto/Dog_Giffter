#!/usr/bin/env python

import json
from random import shuffle
import praw
import requests
import yaml
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon') # we don't use twitter, so we ignore the twypython warning

ANALYZER = SentimentIntensityAnalyzer()
CREDENTIALS = yaml.load(open("credentials.yml", 'r'))
GC = CREDENTIALS["giphy"]["key"]  # giphy CREDENTIALS
RC = CREDENTIALS["reddit"]  # reddit CREDENTIALS

NEGATIVE_THRESHOLD = 0.5
COMPOUND_THRESHOLD = -0.5

dog_pictures = list()

def get_pictures():
    """
    Retrieves dog gifs from GIPHY.
    """
    global dog_pictures
    dog_pictures = requests.get("https://api.giphy.com/v1/gifs/search?api_key=" + GC + "&q=cute dog&limit=1000&offset=0&rating=G&lang=en").json()

    if 'data' in dog_pictures:
        dog_pictures = dog_pictures['data']
        shuffle(dog_pictures)
    else:
        dog_pictures = list()


def analyze_comment(comment):
    """
    Performs sentiment analyzes on the given comment
    """
    scores = ANALYZER.polarity_scores(comment.body) 

    if ( scores['compound'] < COMPOUND_THRESHOLD and scores['neg'] > NEGATIVE_THRESHOLD):
        print(comment.body)
        print(scores)
        reply_to(comment)
        print('==========================================================')


def reply_to(comment):
    """
    Writes a reply to the given comment. This reply contains a cute dog gif.
    """

    if not dog_pictures:
        get_pictures()

    if dog_pictures:
        picture = dog_pictures.pop()
        if 'images' in picture \
        and 'fixed_width' in picture['images'] \
        and 'url' in picture['images']['fixed_width']:
            print('picture =', picture['images']['fixed_width']['url'])
            # print(json.dumps(dog_pictures, sort_keys=True, indent=4))
            # comment.reply("reply text goes here") TODO: uncomment this when reply is ready


def main():
    # reddit instance
    reddit = praw.Reddit(client_id=RC['client_id'], client_secret=RC['client_secret'], user_agent=RC['user_agent'],
                         username=RC['username'], password=RC['password'])

    popular = reddit.subreddit('popular').controversial(limit=1)  # TODO: change limit when sentiment analysis is complete

    for submission in popular:
        submission.comments.replace_more(limit=0)  # remove MoreComments instances
        print("---------------------------------------------------------------------")
        print("title=", submission.title, ", id=", submission.id, ", url=", submission.url, '\n')
        for comment in submission.comments.list():
            analyze_comment(comment)
        print("---------------------------------------------------------------------")


if __name__ == '__main__':
    print('Starting app...')
    print('giphy key: ' + GC)
    print('reddit: ' + str(RC))
    main()
    print('Done!')
