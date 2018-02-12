import numpy as np

def L1(yhat,y):
    """

    :param yhat:
    :param y:
    :return:
    """
    loss = np.sum(np.abs(y - yhat))
    return loss

yhat = np.array([.9,0.2,0.1,.4,.9])
y = np.array([1,0,0,1,1])
print(str(L1(yhat,y)))

def L2(yhat, y):
    loss = np.sum(np.power((y-yhat),2))
    return loss

print("L2 = " + str(L2(yhat, y)))