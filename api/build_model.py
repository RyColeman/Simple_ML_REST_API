import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import pickle

if __name__ == __main__:

    iris = load_iris()

    print('Feature Names of Iris dataset: \n   {0}\n   {1}\n   {2}\n   {3}'.format(iris['feature_names'][0], iris['feature_names'][1], iris['feature_names'][2], iris['feature_names'][3]))

    X = iris['data']
    y = iris['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    clf = GradientBoostingClassifier()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    f1 = f1_score(y_test, y_pred, average='macro')
    print('f1 score: {0:0.2}'.format(f1))

    # Now saving model in a .pkl file:
    pickle.dump(clf, open('models/model.pkl', 'wb'))
