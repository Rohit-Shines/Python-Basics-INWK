import numpy as np
import matplotlib as plt
import numpy as np

x= np.arange(1,15,0.1)
y= np.sin(x)/x
fig, ax = plt.subplots(figsize=(10, 10))
ax.set(title='Plot of x(t) = 2*sin(pi*t+pi/6)',xlabel = '0<=x<=10',ylabel = 'sin(x)/x') # Labeling is important !!
ax.grid(True)
ax.plot(x,y, color='black')