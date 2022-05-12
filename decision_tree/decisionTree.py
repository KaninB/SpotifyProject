import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

raw_data = pd.read_csv('../../Tree/cleaned-edited.csv')

# All relevant attributes
raw_data = raw_data[['Artist.Followers', 'Danceability', 'Energy', 'Loudness',
       'Speechiness', 'Acousticness', 'Liveness', 'Tempo', 'Duration_ms',
       'Valence', 'class', 'explicit', 'mode',
       'instrumentalness', 'time_signature', 'Key']]

# Changes explicit to integer rather than bool
raw_data.explicit = raw_data.explicit.astype('int64')

# Used https://www.analyticsvidhya.com/blog/2021/04/beginners-guide-to-decision-tree-classification-using-python/ for help
# All attributes minus class
x = raw_data.drop('class', axis = 1)
# For classification
y = raw_data['class']

# Taken from Bayes Classifier code
with open("decision_tree_output.t", "w") as f:
    for i in np.arange(0.1,1,0.05):
        i = round(i,2)
        f.write("_"*50 + "\n")
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=i, random_state=0)

        # Decision Tree before pruning
        model = DecisionTreeClassifier(random_state=0)
        model.fit(x_train, y_train)
        y_train_pred = model.predict(x_train)
        y_test_pred = model.predict(x_test)

        # Finds the alpha for pruning the tree
        path = model.cost_complexity_pruning_path(x_train, y_train)
        alphas = path['ccp_alphas']

        accuracy_test = []

        for a in alphas:
               model = DecisionTreeClassifier(ccp_alpha=a)

               model.fit(x_train, y_train)
               y_test_pred = model.predict(x_test)

               accuracy_test.append(accuracy_score(y_test, y_test_pred))

        # Finds alpha from max test accuracy
        max_value = max(accuracy_test)
        max_index = accuracy_test.index(max_value)
        alpha = alphas[max_index]

        # New decision tree
        model = DecisionTreeClassifier(ccp_alpha=alpha, random_state=0)
        model.fit(x_train, y_train)
        y_test_pred = model.predict(x_test)

        # Prints accuracy, precision, and recall
        f.write("Train %: {0} Test %: {1} \n".format(i, round(1-i,2)))

        f.write(f"{classification_report(y_test, y_test_pred)} \n")
        f.write(f"{confusion_matrix(y_test, y_test_pred)} \n")

# Example visual of a tree of training size 70% and testing 30%
x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x, y, test_size = 0.3, random_state=0)

model = DecisionTreeClassifier(random_state=0)
model.fit(x_training_data, y_training_data)
y_train_pred = model.predict(x_training_data)
y_test_pred = model.predict(x_test_data)

# Referenced from https://www.analyticsvidhya.com/blog/2020/10/cost-complexity-pruning-decision-trees/
path = model.cost_complexity_pruning_path(x_training_data, y_training_data)
alphas = path['ccp_alphas']

accuracy_train, accuracy_test = [],[]

for i in alphas:
    model = DecisionTreeClassifier(ccp_alpha = i)

    model.fit(x_training_data, y_training_data)
    y_test_pred = model.predict(x_test_data)

    accuracy_test.append(accuracy_score(y_test_data, y_test_pred))

max_value = max(accuracy_test)
max_index = accuracy_test.index(max_value)
alpha = alphas[max_index]

model = DecisionTreeClassifier(ccp_alpha=alpha, random_state=0)
model.fit(x_training_data, y_training_data)
y_train_pred = model.predict(x_training_data)
y_test_pred = model.predict(x_test_data)

features = ['Artist.Followers', 'Danceability', 'Energy', 'Loudness',
       'Speechiness', 'Acousticness', 'Liveness', 'Tempo', 'Duration_ms',
       'Valence', 'explicit', 'mode',
       'instrumentalness', 'time_signature', 'Key']

# Found from https://mljar.com/blog/visualize-decision-tree
# Saves the log and prints the tree
with open("decision_tree.log", "w") as fout:
    fout.write(tree.export_text(model, feature_names = features))

_ = tree.plot_tree(model, feature_names = raw_data.columns, filled=True)
plt.show()
