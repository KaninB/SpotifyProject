import numpy as np
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.feature_selection import SelectFromModel

input_file = os.path.dirname(os.getcwd()) + "\\bayes_classifier\\cleaned-edited.csv"

df = pd.read_csv(input_file, header=0)
original_headers = list(df.columns.values)
df = df._get_numeric_data()
numeric_headers = list(df.columns.values)
X = df.to_numpy()

# First 1556 values are Top 200
top_len = 1556
y1 = [1 for i in range(1,top_len+1)] #Offset of one required for range
y2 = [0 for j in range(1, len(X)-top_len+1)] #Offset of one required for range
y = y1 + y2


# Run model for various combinations of train and test
with open("bayes_output.t", "w") as f:
    for i in np.arange(0.1,1,0.05):
        i = round(i,2)
        f.write("_"*50 + "\n")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=i, random_state=0)
        gnb = GaussianNB()
        y_pred = gnb.fit(X_train, y_train).predict(X_test)
        f.write("Train %: {0} Test %: {1} \n".format(round(1-i,2), round(i,2)))
        f.write("Number of mislabeled points out of a total %d points : %d \n" % (X_test.shape[0], (y_test != y_pred).sum()))
        f.write(f"Acc: {round(accuracy_score(y_test, y_pred),2)} \n")
        f.write(f"Prec: {round(precision_score(y_test, y_pred),2)} \n")
        f.write(f"Rec: {round(recall_score(y_test, y_pred),2)} \n")
