import numpy as np
import pandas as pd
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.feature_selection import SelectFromModel

input_file = os.path.dirname(os.getcwd()) + "\\random_forest\\cleaned-edited.csv"

df = pd.read_csv(input_file, header=0)
df = df._get_numeric_data()
X = df.to_numpy()

# First 1556 values are Top 200
top_len = 1556
y1 = [1 for i in range(1,top_len+1)] #Offset of one required for range
y2 = [0 for j in range(1, len(X)-top_len+1)] #Offset of one required for range
y = y1 + y2

with open("random_forest.txt", "w") as f:
    f.write("_"*50+"\n")
    i=0.3
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=i)
    clf = RandomForestClassifier(min_impurity_decrease=0.03, max_depth=5)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    model = SelectFromModel(clf, prefit=True, threshold=0.05)
    X_new = model.transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=i)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    f.write(f"Accuracy Report: {classification_report(y_test, y_pred)}")
    f.write("Train %: {0} Test %: {1} \n".format(round(1-i,2), round(i,2)))
    f.write("Number of mislabeled points out of a total %d points : %d \n" % (X_test.shape[0], (y_test != y_pred).sum()))
    f.write(f"Acc: {round(accuracy_score(y_test, y_pred),2)} \n")
    f.write(f"Prec: {round(precision_score(y_test, y_pred),2)} \n")
    f.write(f"Rec: {round(recall_score(y_test, y_pred),2)} \n")