#install nltk
#install textblob
#install newspaper 3k

#Sentiment from input.txt

from textblob import TextBlob
from newspaper import Article

with open("input.txt", 'r') as f:
    text = f.read()
'''
input.txt = "I am very Happy!" positive
input.txt = "1 times 1 is 1" is Neutral
input.txt = "I hate you!" Negative
'''

print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity #-1 to 1
print(sentiment)


'''
Sentiment from article
from textblob import TextBlob
from newspaper import Article

#url ="https://en.wikipedia.org/wiki/Mathematics" positive
#url = "https://www.foxla.com/news/pomona-crash-3-women-killed" negative
#url = "https://www.hopkinsmedicine.org/health/wellness-and-prevention/the-power-of-positive-thinking" positive
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity #-1 to 1
print(sentiment)
'''