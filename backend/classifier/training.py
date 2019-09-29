

# importing library
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import numpy as np
import json
import dump

# loading the npy files for training of model
X_train = np.load('../dataset/X_train.npy')
y_train = np.load('../dataset/y_train.npy')
print('X_train:{0}, y_train:{1}'.format(X_train.shape, y_train.shape))

# Using CLF for random forest, calculation for CV is calculated
clf = RandomForestClassifier()
print('Cross Validation Score: {0}'.format(np.mean(cross_val_score(clf, X_train, y_train, cv=10))))

clf.fit(X_train, y_train)

# loading test to calculate the accuracy of the model is calculated
X_test = np.load('../dataset/X_test.npy')
y_test = np.load('../dataset/y_test.npy')

pred = clf.predict(X_test)
print('Accuracy: {}'.format(accuracy_score(y_test, pred)))

# print(forest_to_json(clf))
json.dump(dump.forest_to_json(clf), open('../../static/classifier.json', 'w'))

