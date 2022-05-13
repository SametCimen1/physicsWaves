import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-4,4,200)



# setting the axes at the center
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the functions, with labels
p = np.sin(x) 
# q = np.sin(5*x) 
# u = 3 * np.sin(10*x) #green wave
# r = np.sin(2*x-2)+1

plt.plot(x,p, 'b-', label='y=sin(x)')
# plt.plot(x,q, 'c-', label='y=sin(5x)')
# plt.plot(x,u, 'g-', label='y=3sin(x)')
# plt.plot(x,r, 'r-', label='y=sin(2x-2)+1')

plt.legend(loc='upper left')

# show the plot
plt.show()