# CHAPTER 8
# CASCADING IN SOCIAL NETWORKS
# IMPORTING LIBRARIES
import networkx as nx
import matplotlib.pyplot as plt
import random
# RANDOM GRAPH - Erdős-Rényi
n = 100  # NODES COUNTS
m = 300  # EDGES COUNTS
graph1 = nx.gnm_random_graph(n, m)
# GRAPH PLOT
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(graph1)
nx.draw(graph1, pos, node_size=10, node_color='red', edge_color='green', alpha=0.7, with_labels=True)
plt.title(" Erdős-Rényi (n=100، m=300) RANDOM GRAPH")
plt.show()

print("Problem 50 Results by Armin Zakarian")

