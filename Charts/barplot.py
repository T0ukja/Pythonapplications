import numpy as np
import matplotlib.pyplot as plt

height = [25, 30, 12, 5, 16]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

plt.bar(y_pos, height)

plt.xticks(y_pos, bars)

plt.show()
