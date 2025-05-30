from textblob import TextBlob

def detect_sentiment(text):
    """
    Analyze sentiment of the input text using TextBlob.
    Retuns: 'positive', 'negative', or 'neutral'
    """

    blob=TextBlob(text)
    polarity = blob.sentiment.polarity # range: [-1,1]

    if polarity > 0.2:
        return 'positive'
    elif polarity < -0.2:
        return 'negative'
    else:
        return 'neutral'