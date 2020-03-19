# Quick example of the stemming

from porter import PorterStemmer

porter = PorterStemmer()

words = ["dogs", "cats", "cafes", "shops", "bookshops", "bars"]

for w in words:
    print("Word: {0} -- Stem: {1}".format(w, porter.stem(w)))