import numpy as np
import sklearn
import sklearn.linear_model
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import sklearn.datasets

from planar_utils.planar_utils import *
X, Y = load_planar_dataset()
print(Y.T.shape)
clf = sklearn.linear_model.LogisticRegressionCV()
clf.fit(X.T, Y.T.ravel())

#use below code to output the decision boundary

plot_decision_boundary(lambda x:clf.predict(x), X, Y)
plt.title('logistic regression')

#print accuracy
LR_predictions = clf.predict(X.T)
print("accuracy of logistic regression: %d" % float((np.dot(Y,LR_predictions) + np.dot(1-Y,1-LR_predictions))/float(Y.size)*100) +
       '% ' + "(percentage of correctly labelled datapoints)")
