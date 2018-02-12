import numpy as np
import time
x1 = [9,2,5,0,0,7,0,0,0,9,2,5,0,0]
x2 = [9,2,2,9,0,9,2,5,0,0,9,2,5,0]

#use Vectorized dot to calculate
tic = time.process_time()
dot = np.dot(x1,x2)
toc = time.process_time()

print("dot = " + str(dot) + "\n----computation time = "+str(1000*(toc-tic)))

#use to calculate outer

tic = time.process_time()
outer = np.outer(x1,x2)
toc = time.process_time()

print("outer = " + str(outer) + "\n----computation time = "+str(1000*(toc-tic)))


#elementwise calculate
tic = time.process_time()
mul = np.multiply(x1,x2)
toc = time.process_time()
print("mul = " + str(mul) + "\n----computation time = "+str(1000*(toc-tic)))

#general dot
W = np.random.rand(3,len(x1))
tic = time.process_time()
dot1 = np.dot(W,x1)
toc = time.process_time()

print("dot1 = " + str(dot1) + "\n----computation time = "+str(1000*(toc-tic)))










