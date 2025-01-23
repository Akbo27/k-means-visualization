import numpy as np
import matplotlib.pyplot as plt
import random

initial_centroids = [(2, 3), (7, 8), (3, 9)] 
num_points = 300

def generate_points(centroid, num_points, std_dev):
    cx, cy = centroid
    points = []
    for _ in range(num_points):
        x = random.gauss(cx, std_dev)  
        y = random.gauss(cy, std_dev)
        points.append((x, y))
    return points

all_points = []
for centroid in initial_centroids:
    all_points.extend(generate_points(centroid, 300, std_dev=1.0))  

plt.figure(figsize=(8, 6))
for centroid in initial_centroids:
    plt.scatter(*centroid, color='red', s=100, label="Centroid")  

points_x = [p[0] for p in all_points]
points_y = [p[1] for p in all_points]
plt.scatter(points_x, points_y, s=10, alpha=0.7, label="Points")

plt.title("Random Points Around Guessed Centroids")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.savefig("guessed_centroids_plain.png") 
plt.show()

    


