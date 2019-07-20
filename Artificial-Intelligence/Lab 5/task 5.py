import pandas as pd
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import re
train = pd.read_csv('C:\Users\Mujtaba Faizi\Downloads\labeledTrainData.tsv', header=0, delimiter='\t', quoting=3)
example1 = BeautifulSoup(train["review"][0],"lxml")
a= example1.get_text()
print a
#replacing upercase letters with space character
example_ = re.sub('[^A-Za-z0-9]+'," ",a)
print example_
#convert every thing into lower case and split the reviews into individual words
words = example_.lower().split()
for b in words:
    print b
print "removing all english stopwords"
nltk.download('stopwords')
stops = set(stopwords.words('english'))
words = [w for w in words if not w in stops]
for b in words:
    print b
#Now join the words back into one string separated by :
sentence = ":".join(words)
print sentence
