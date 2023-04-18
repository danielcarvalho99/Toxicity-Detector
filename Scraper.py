def check_user_existence(scraper):
    pass


def get_tweets(scraper, number_of_tweets):
    tweets = []

    for i, tweet in enumerate(scraper.get_items()):
        tweets.append(tweet.rawContent)
        if i == number_of_tweets:
            return tweets