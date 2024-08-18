import matplotlib.pyplot as plt
import numpy as np

# Given data
center = (2, -3)
A = (3, -10)
B = (1, 4)

# Calculate the radius using the distance formula
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
radius = distance(center, A) #Using radius as a variable eliminates having to enter the value of the radius, sqrt(50).

#Plot Circle
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = center[0] + radius * np.cos(theta)
y_circle = center[1] + radius * np.sin(theta)

plt.figure(figsize=(8, 8))
plt.plot(x_circle, y_circle, label='Circle')  

# Plot Points
plt.scatter(*center, color='red', label='O (2, -3)')
plt.scatter(*A, color='red', label='A (3, -10)')
plt.scatter(*B, color='red', label='B (1, 4)')

# Mark the diameter
plt.plot([A[0], B[0]], [A[1], B[1]], 'k--', label='Diameter')

# Coordinates
plt.text(center[0], center[1], f' O\n{center}', fontsize=12, ha='right', color='red')
plt.text(A[0], A[1], f'  A\n{A}', fontsize=12, ha='right', color='red')
plt.text(B[0], B[1], f'  B\n{B}', fontsize=12, ha='right', color='red')

# Setting labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('A plot of the circle and the lines involved')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal')  # Equal scaling for x and y axes

# Show the plot
plt.show()

