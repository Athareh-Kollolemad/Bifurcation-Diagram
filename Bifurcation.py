import matplotlib.pyplot as plt
import numpy as np
p = np.linspace(0.7, 4, 100000)
m = 0.7
x = []
y = []
for u in p:
    x.append(u)
    m = np.random.random()
    for n in range(1001):
        m = (u*m)*(1-m)
    for i in range(1051):
        m = (u*m)*(1-m)
    y.append(m)
plt.plot(x, y, ls=' ', marker=',')
plt.xlabel('X')
plt.ylabel("alfa")
plt.show()
