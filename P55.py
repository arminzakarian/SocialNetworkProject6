# CHAPTER 8
# CASCADING IN SOCIAL NETWORKS
# IMPORTING LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
T = [1, 1, 1, 1, 1, 4, 1, 0, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 4, 0, 1, 4, 0, 1, 1, 1, 4, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 4, 1, 1, 4, 1, 4, 0, 1, 0, 1, 1, 1, 0, 4, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 4, 0, 4, 0, 0, 1, 1, 1, 4, 0, 4, 0]
N, bins, patches = plt.hist(T, bins=np.arange(len(set(T))) + 0.5, align='mid', rwidth=0.5)
plt.xlabel('THRESHOLD')
plt.ylabel('FREQUENCY')
plt.title('HISTOGRAM OF THRESHOLDS')
plt.xticks(np.arange(len(set(T))) + 0.5, np.arange(len(set(T)))+1)
plt.show()
print("Problem 55 Results by Armin Zakarian")