import random
import data
from classifier import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn import tree

stats = data.getData()
positions = data.getPositions()

X_train, X_test, y_train, y_test = train_test_split(stats, positions, test_size = .5)

my_classifier = KNeighborsClassifier()
my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)
print (predictions)

from sklearn.metrics import accuracy_score
print (accuracy_score(y_test, predictions))
