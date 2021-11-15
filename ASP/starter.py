import numpy as np 
import matplotlib.pyplot as plt 
import librosa as l 

x =  np.linspace(0,10,50)

y =  np.sin(x) + np.random.normal(0,0.34,50)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("sin(x) + N(0,0.34)")
plt.title("Simple Stochastic Random Process")
plt.show()
