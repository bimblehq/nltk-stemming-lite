# Quick example of the stemming

from porter import PorterStemmer
from lancaster import LancasterStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()

words = ["dogs", "cats", "cafes", "shops", "bookshops", "bars", "cafe",  "columbia", "coffee", "coffees", "outdoors"]

for w in words:
    print("Word: {0}".format(w))
    print("Stem: {0}".format(porter.stem(w)))
    print("======")
