from textblob.blob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from main import headlines
import textblob

'''
Method to return the sentiment and polarity of each headline
params:
arr: list: array which contain string values(headlines)
'''

def get_sentiment(arr:list):
    for i in arr:
        return TextBlob(i,analyzer=NaiveBayesAnalyzer()).sentiment

print(get_sentiment(headlines))