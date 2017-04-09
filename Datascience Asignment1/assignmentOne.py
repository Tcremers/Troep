import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors
import numpy as np


fig, ax = plt.subplots()
print ax.get_children()
line = ax.scatter(0,0)

for i in range(10):
    ax.draw(ax.patch)
plt.show()