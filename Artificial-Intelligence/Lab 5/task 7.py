import pandas as pd
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import re

def review_to_words(raw_review,n):
    example1 = BeautifulSoup(raw_review["review"][n], "lxml")
    a = example1.get_text()
    example_ = re.sub('[^A-Za-z0-9]+', " ", a)
    words = example_.lower().split()
    nltk.download('stopwords')
    stops = set(stopwords.words('english'))
    words = [w for w in words if not w in stops]
    # Now join the words back into one string separated by :
    sentence = ":".join(words)
    return sentence

train = pd.read_csv('C:\Users\Mujtaba Faizi\Downloads\labeledTrainData.tsv', header=0, delimiter='\t', quoting=3)
review_list=[]
i=0
for a in train:
    b=review_to_words(train,i)
    review_list.append(b)
    i=i+1
print review_list