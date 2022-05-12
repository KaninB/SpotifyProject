import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/cleaned-edited.csv')
X = data.iloc[:, [3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 21, 23, 24]]
y = data.loc[:, "class"].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(max_iter=1000)
mlp.fit(X_train, y_train)
# hidden_layer_sizes=(10, 5),
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
predictions_train = mlp.predict(X_train)
print("Train accuracy: ", accuracy_score(predictions_train, y_train))
predictions_test = mlp.predict(X_test)
print("Test accuracy: ", accuracy_score(predictions_test, y_test))
print(confusion_matrix(predictions_train, y_train))



print(confusion_matrix(predictions_test, y_test))
print(classification_report(y_test, predictions_test))

# fig, axes = plt.subplots(1, 1)
# axes.plot(mlp.loss_curve_, 'o-')
# axes.set_xlabel("number of iteration")
# axes.set_ylabel("loss")
# plt.show()
#
