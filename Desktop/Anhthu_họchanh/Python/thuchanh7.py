from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
# iris = load_iris()
# print(iris)
# print(iris.data[1:5])
# print(iris.target[1:5])
# print(iris.target_names)

# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, train_size=2/3.0, random_state=5)

# X_train[1:6]1
# X_train[1:6, 1:3]
# y_train[1:6]
# X_test[6:10]
# y_test[6:10]

#print(X_train[:6], X_test[:6])

# clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)
# clf_gini.fit(X_train, y_train)
# y_pred = clf_gini.predict(X_test)
# y_test
# pv = clf_gini.predict([[4, 6, 3, 3]])
# print(pv)
# print(y_test)
# print(y_pred)

# print("Accuracy is", accuracy_score(y_test, y_pred)*100)
# print(confusion_matrix(y_test, y_pred, labels=[2, 0, 1]))

import pandas as pd
import numpy as np
# dt5 = pd.read_csv("dataset\iris.csv")
# # dt5[1:5]
# print(len(dt5))
# # dt5.petalLength[1:5]
# print(dt5)

housing = pd.read_csv("dataset\housing_RT.csv", index_col=0)
print(housing.iloc[1:5, ])

X_train, X_test, y_train, y_test = train_test_split(housing.iloc[:, 1:5], housing.iloc[:,0],test_size=1/3.0, random_state=100)
X_train[1:5]
X_test[1:5]

print("TRAIN", X_train)
print("TEST", X_train)

regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
y_test[1:5]
y_pred[1:5]

print(y_test)
print(y_pred)

err = mean_squared_error(y_test, y_pred)
err
print(np.sqrt(err))
print(err)
