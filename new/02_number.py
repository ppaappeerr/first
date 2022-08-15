import matplotlib.pyplot as plt
import numpy as np

dict = {'data_x':[1, 2, 3, 4, 5], 'data_y':[2, 3, 5, 10, 8]}
plt.plot('data_x', 'data_y', data=dict)
plt.show()