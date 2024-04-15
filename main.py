#install nltk
#install textblob
#install newspaper 3k

from textblob import TextBlob
from newspaper import Article

#url ="https://en.wikipedia.org/wiki/Mathematics" positive
#url = "https://www.foxla.com/news/pomona-crash-3-women-killed" negative
url = "https://www.hopkinsmedicine.org/health/wellness-and-prevention/the-power-of-positive-thinking"
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity #-1 to 1
print(sentiment)