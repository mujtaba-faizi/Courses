import pandas as pd

train = pd.read_csv('C:\Users\Mujtaba Faizi\Downloads\labeledTrainData.tsv', header=0, delimiter='\t', quoting=3)
print train.shape
print train.head(10)