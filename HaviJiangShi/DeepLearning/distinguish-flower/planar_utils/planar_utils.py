import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# from testCases import *
import sklearn
import sklearn.datasets
import sklearn.linear_model

def load_planar_dataset():
    np.random.seed(1) #set a seed so the results are consistent
    #样本的数量
    m = 400
    #the num of example,每个
    N = int(m/2)
    #维度
    D = 2
    #初始化X~(400,2)
    X = np.zeros((m, D))
    Y = np.zeros((m, 1), dtype='uint8')
    #花儿的最大长度
    a = 4

    for j in range(2):
        ix = range(N*j, N*(j+1))
        t = np.linspace(j*3.12,(j+1)*3.12,N) + np.random.randn(N)*0.2
        r = a*np.sin(4*t) + np.random.randn(N)*0.2
        X[ix] = np.c_[r*np.sin(t),r*np.cos(t)]
        Y[ix] = j

    X = X.T
    Y = Y.T
    return X, Y
#use mat

# X ,Y = load_planar_dataset()
# print("inital data X:" + str(X))
# print("\n" + "inital data: Y" + str(Y))
# shape_X = X.shape
# shape_Y = Y.shape
# print('the shape of X is :' + str(shape_X))
# print('the shape of Y is :' + str(shape_Y))
# plt.scatter(X[0, :],X[1, :], c=Y, s=40, cmap=plt.cm.Spectral)

def plot_decision_boundary(model, X, y):
    #set min and max values and give it some padding
    x_min, x_max = X[0, :].min() - 1, X[0, :].max() + 1
    y_min, y_max = X[1, :].min() - 1, X[1, :].max() + 1
    h = 0.01
    #generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    #predict the function value for the whole grid
    Z = model(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    #plot the contour and training examples
    # plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    # plt.ylabel('x2')
    # plt.xlabel('x1')
    # plt.scatter(X[0, :], X[1, :], c=y, cmap=plt.cm.Spectral)

def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(x)
    """
    s = 1/(1+np.exp(-x))
    return s









