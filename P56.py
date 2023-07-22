# CHAPTER 8
# CASCADING IN SOCIAL NETWORKS
# IMPORTING LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
T = [1, 1, 1, 1, 1, 4, 1, 0, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 4, 0, 1, 4, 0, 1, 1, 1, 4, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 4, 1, 1, 4, 1, 4, 0, 1, 0, 1, 1, 1, 0, 4, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 4, 0, 4, 0, 0, 1, 1, 1, 4, 0, 4, 0]
N = np.cumsum(np.histogram(T, bins=np.arange(len(set(T))) + 0.5)[0])
plt.plot(N)
plt.xlabel('THRESHOLD')
plt.ylabel('CUMULATIVE FREQUENCY')
plt.title('CUMULATIVE HISTOGRAM OF THRESHOLDS')
plt.show()
final_number_of_rioters = N[-1]
print('Final number of rioters:', final_number_of_rioters)
print("Problem 56 Results by Armin Zakarian")