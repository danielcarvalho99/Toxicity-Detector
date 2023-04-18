def predict_tweet(tweet, pipeline):
    label = pipeline(tweet)[0]['label']
    if label == 'LABEL_0':
        return 0
    else:
        return 1

def get_predictions(tweets, pipeline):
    predictions = []
    for tweet in tweets:
        predictions.append(predict_tweet(tweet, pipeline))
    return predictions