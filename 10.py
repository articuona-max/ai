import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

text = "perform tokenization in this random algorithm"

tokens = word_tokenize(text)
'''
nltk.download('punkt')
nltk.download('stopwords')'''

stopwords = set(stopwords.words('english'))

filtered_words = [word for word in tokens if word not in stopwords and word.isalpha()]
stemmed_words  = [PorterStemmer().stem(word) for word in filtered_words]
print(stemmed_words)
