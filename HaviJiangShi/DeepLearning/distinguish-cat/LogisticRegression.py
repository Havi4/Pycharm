import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from lr_utils.lr_utils import load_dataset

train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
index = 25
print("train_set_x_orig=" + str(test_set_x_orig) + "\n----rank is :" + str(train_set_x_orig.shape))
# plt.imshow(train_set_x_orig[index])
# plt.show()
print("y = " + str(train_set_y[:, index]) + ", it's a " + str(classes[np.squeeze(train_set_y[:,index])].decode("utf-8")) + "picture")
###start code here ###
m_train = train_set_x_orig.shape[0]
m_test = test_set_x_orig.shape[0]
num_px = train_set_x_orig.shape[1]
###code end###
print("Number of training examples: m_train = " + str(m_train))
print("Number of test examples: m_test = " + str(m_test))
print("Height/Width of each image: num_px = " + str(num_px))
print("Each image is of size: (" + str(num_px) + ", " + str(num_px) + ", 3)")
print("train_set_x shape: " + str(train_set_x_orig.shape))
print("train_set_y shape: " + str(train_set_y.shape))
print("test_set_x shape: " + str(test_set_x_orig.shape))
print("test_set_y shape: " + str(test_set_y.shape))

#reshape the training and test examples
train_set_x_flatten = train_set_x_orig.reshape(m_train, -1).T
test_x_flatten = test_set_x_orig.reshape(m_test, -1).T

print("train_set_x_flatten shape:" + str(train_set_x_flatten.shape))
print("train_set_y shape:" + str(train_set_y.shape))
print("test_set_x_flatten shape:" + str(test_x_flatten.shape))
print("test_set_y shape:" + str(test_set_y.shape))

#center and standardize the the dataset
train_set_x = train_set_x_flatten/255.0
test_set_x = test_x_flatten/255.
print("standardized data:" + str(train_set_x) + "\n" + str(test_set_x))

#grade function

def sigmoid(z):
    """
    compute the sigmoid of z
    :param z:
    :return:
    """
    s = 1.0/(1 + np.exp(-z))
    return s

#grade function: initialize_with_zeros

def initialize_with_zeros(dim):
    w = np.zeros((dim, 1))
    b = 0
    assert(w.shape == (dim, 1))
    assert(isinstance(b, float) or isinstance(b, int))
    return w, b
print("initial value " + str(initialize_with_zeros(2)))

#to calculate cost function

def propagate(w, b, X, Y):
    m = X.shape[1]

    ###forward propagation from x to cost
    A = sigmoid(np.dot(w.T, X) + b)
    cost = -(1.0/m)*np.sum(Y*np.log(A) + (1-Y)*np.log(1-A))

    ###backward propagation (to find grade)
    dw = (1.0/m)*np.dot(X, (A-Y).T)
    db = (1.0/m)*np.sum(A-Y)
    ##end

    assert (dw.shape == w.shape)
    assert (db.dtype == float)
    cost = np.squeeze(cost)
    assert (cost.shape == ())

    grads = {"dw": dw,
             "db": db
             }
    return grads, cost

w = np.array([[1.],[2.]])
b = 2.
X = np.array([[1.,2.,-1.],[3.,4.,-3.2]])
Y = np.array([[1,0,1]])
grads, cost = propagate(w, b, X, Y)
print("dw = " + str(grads["dw"]))
print("db = " + str(grads["db"]))
print("cost = " + str(cost))


###grade function: optimize

def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost = False):
    costs = []

    for i in range(num_iterations):
        #cost and gradient calculation
        grads, cost = propagate(w, b, X, Y)

        dw = grads["dw"]
        db = grads["db"]

        ###update rule
        w = w - learning_rate*dw
        b = b - learning_rate*db

        #record the costs

        if i%100 == 0:
            costs.append(cost)

        if print_cost and i % 100 == 0:
            print("cost after iteration %i: %f" %(i, cost))

    params = {
        "w": w,
        "b": b
    }

    grads = {
        "dw": dw,
        "db": db
    }

    return params, grads, costs


params, grads, costs = optimize(w, b, X, Y, num_iterations=100, learning_rate= 0.009, print_cost= False)
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("w = " + str(params["w"]))
print("b = " + str(params["b"]))
print("dw = " + str(grads["dw"]))
print("db = " + str(grads["db"]))

#grade function :predict

def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    A = sigmoid(np.dot(w.T, X) + b)

    for i in range(A.shape[1]):
        if A[0, i] > 0.5:
            Y_prediction[0, i] = 1
        else:
            Y_prediction[0, i] = 0
    assert (Y_prediction.shape == (1, m))
    return Y_prediction




w = np.array([[0.1124579],[0.23106775]])
b = -0.3

X = np.array([[1.,-1.1,-3.2],[1.2,2.,0.1]])

print("prediction = " + str(predict(w, b, X)))




#grade Model

def model(X_train, Y_train, X_test, Y_test, num_iterations = 2000, learning_rate = 0.5, print_cost = False):
    ##initial params
    w, b = initialize_with_zeros(X_train.shape[0])

    #gradient descent
    parameters, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)

    #retrieve parameters w and b from dictionary "parameters"
    w = parameters["w"]
    b = parameters["b"]

    #price
    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)

    print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test,
         "Y_prediction_train": Y_prediction_train,
         "w": w,
         "b": b,
         "learning_rate": learning_rate,
         "num_iterations": num_iterations}
    return d

d = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations=2000, learning_rate=0.005, print_cost= True)

costs = np.squeeze(d["costs"])
plt.plot(costs)
plt.ylabel("cost")
plt.xlabel("iterations (per hundreds)")
plt.title("learning rate =" + str(d["learning_rate"]))
plt.show()
print(d)

learning_rates = [0.01, 0.001, 0.0001]
models = {}

for i in learning_rates:
    print("learning rate is:" + str(i))
    models[str(i)] = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations= 1500, learning_rate= i, print_cost= False)
    print("\n" + "--------------------------------------")

for i in learning_rates:
    plt.plot(np.squeeze(models[str(i)]["costs"]), label= str(models[str(i)]["learning_rate"]))

plt.ylabel("cost")
plt.xlabel("iterations")

legend = plt.legend(loc="upper center",shadow = True)
frame = legend.get_frame()
frame.set_facecolor('0.9')
plt.show()

my_images = "cat2.jpg"
fname = my_images
image = np.array(ndimage.imread(fname, flatten=False))
my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((1, num_px*num_px*3)).T
my_predicted_image = predict(d["w"], d["b"], my_image)
plt.imshow(image)

print("y = " + str(np.squeeze(my_predicted_image)) + ", your algorithm predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")
plt.show()



