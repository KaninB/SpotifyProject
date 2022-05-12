import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, recall_score
data = pd.read_csv('../data/cleaned-edited.csv')
data.explicit = data.explicit.astype('int64') #transform explicit as number
X = data.iloc[:, [3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 21, 22, 23, 24]]
y = data.loc[:, "class"].values

#Split data for testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)

# Normalize data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Initial Classifier
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
score = classifier.score(X_train, y_train)
print("Training score: ", score)
print(classification_report(y_test, y_pred))


# FEATURE SELECTION
# I ran this starting with 1 attribute then adding on more based off the earlier results. My metric was recall because of the class imbalance problem
# Most important: 3 (Artist Following), 19 Time signature, explicit
feat_lists = [
    [3], [8], [9], [10], [11], [12], [13], [14], [15], [16], [19], [21], [22], [23], [24],
    [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [3, 15], [3, 16], [3, 19], [3, 21], [3, 22], [3, 23], [3, 24],
    [3, 23, 8], [3, 23, 9], [3, 23, 10], [3, 23, 11], [3, 23, 12], [3, 23, 13], [3, 23, 14], [3, 23, 15], [3, 23, 16], [3, 23, 19], [3, 23, 21], [3, 23, 22], [3, 23, 24]
]
accuracy = [0] * len(feat_lists)
recall = [0] * len(feat_lists)
index=0
for feature in feat_lists:
    X = data.iloc[:, feature]
    y = data.loc[:, "class"].values
    # Split data for testing
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)
    # Norm
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    from sklearn.neighbors import KNeighborsClassifier
    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    # from sklearn.metrics import accuracy_score
    # print(accuracy_score(y_test, y_pred))
    accuracy[index] = accuracy_score(y_test, y_pred)
    recall[index] = recall_score(y_test, y_pred)
    index = index+1
print(accuracy)
print(max(accuracy))
max_index = accuracy.index(max(accuracy))
print(max_index)
print(recall)
print(recall.index(max(recall)))


X = data.iloc[:, [3]]
y = data.loc[:, "class"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Tuning the number of neighbors to look at
from sklearn.model_selection import GridSearchCV
parameters = {"n_neighbors": range(1, 20)}
gridsearch = GridSearchCV(KNeighborsClassifier(), parameters, scoring='recall')
gridsearch.fit(X_train, y_train)
print(gridsearch.best_params_) #1 neighbor

# Retraining the Model
classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
score = classifier.score(X_train, y_train)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Look at results
# from sklearn.metrics import classification_report, confusion_matrix
# print(classification_report(y_test, y_pred))
# print(confusion_matrix(y_test, y_pred))

# Look more at precision and recall because our data set is imbalanced.
# from sklearn.metrics import accuracy_score
# print(accuracy_score(y_test, y_pred))
