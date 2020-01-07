import numpy as np
import matplotlib.pyplot as plt

data = [0.5, 0.7, 0.1, 2, 1, 1]
r = np.random.random(6)

# plotting data
plt.plot(data, label='test data', c='b')
plt.plot(r, label='random data', c='r')
plt.legend()

# labelling plot
plt.title('plot title')
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.show()
