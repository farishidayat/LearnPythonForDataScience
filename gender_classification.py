import numpy as np
from sklearn import tree

clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']
value = [[190, 70, 43]]

# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)

prediction = clf.predict(value)
print("Decision Tree Prediction = ", prediction)

# CHALLENGE - create 3 more classifiers...
# 1 Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier

# 2 AdaBoost
from sklearn.ensemble import AdaBoostClassifier

# 3 Gaussian Process
from sklearn.gaussian_process import GaussianProcessClassifier

# CHALLENGE compare their results and print the best one!
# Training and Test Sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y)

# Metrics Accuracy Score
from sklearn.metrics import accuracy_score

# 1 Nearest Neighbors Prediction
neigh = KNeighborsClassifier()
neigh = neigh.fit(X,Y)
prediction_neigh = neigh.predict(value)
# Calculate accuracy score
AccNeigh = neigh.fit(X_train, y_train)
AccNeigh = AccNeigh.predict(X_test)
accuracy_neigh = accuracy_score(y_test, AccNeigh)
#Print The Prediction and The Accuracy
print("Nearest Neighbors Prediction = ", prediction_neigh)
print("Nearest Neighbors Accuracy = " + str(round(accuracy_neigh*100,2)) + "%")

# 2 AdaBoost Prediction
Ada = AdaBoostClassifier()
Ada = Ada.fit(X,Y)
prediction_Ada = Ada.predict(value)
# Calculate accuracy score
AccAda = Ada.fit(X_train, y_train)
AccAda = AccAda.predict(X_test)
accuracy_Ada = accuracy_score(y_test, AccNeigh)
#Print The Prediction and The Accuracy
print("AdaBoost Prediction = ", prediction_Ada)
print("AdaBoost Accuracy = "+ str(round(accuracy_Ada*100,2)) + "%")

# 3 Gaussian Process Prediction
Gaussian = GaussianProcessClassifier()
Gaussian = Gaussian.fit(X,Y)
prediction_Gauss = Gaussian.predict(value)
# Calculate accuracy score
AccGauss = Gaussian.fit(X_train, y_train)
AccGauss = AccGauss.predict(X_test)
accuracy_Gauss = accuracy_score(y_test, AccGauss)
#Print The Prediction and The Accuracy
print("Gaussian Process Prediction = ", prediction_Gauss)
print("Gaussian Process Accuracy = "+ str(round(accuracy_Gauss*100,2)) + "%")