import subprocess
import matplotlib.pyplot as plt

# Call the C program and capture its output
result = subprocess.run(["./vector_calculator"], capture_output=True, text=True, check=True)

# Process the output
lines = result.stdout.strip().split('\n')
normal_vector = eval(lines[0].strip().split(': ')[1])  # Extract and evaluate normal vector
direction_vector = eval(lines[1].strip().split(': ')[1])  # Extract and evaluate direction vector

# Extract line points from the output line
line_points_str = lines[2].strip().split(': ')[1]
line_points = eval('[' + line_points_str + ']')  # Convert string to list of tuples

# Separate line points into x and y coordinates
x_line, y_line = zip(*line_points)

# Choose a point on the line to place the vectors (e.g., x = 20)
x_vector_point = 20
y_vector_point = 5 * x_vector_point - 100  # Calculate corresponding y value

# Scale down the vectors to 2/3 of their current length
normal_vector_scaled = [v * (2/3) for v in normal_vector]  # Scale normal vector
direction_vector_scaled = [-v * (2/3) for v in direction_vector]  # Flip and scale direction vector

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the original line
plt.plot(x_line, y_line, 'k--', label='Line: 5x - y = 100', alpha=0.5)  # Dashed line

# Plot the normal vector starting from the point on the line
plt.quiver(x_vector_point, y_vector_point, normal_vector_scaled[0], normal_vector_scaled[1], color='darkblue', angles='xy', scale_units='xy', scale=1,
           width=0.01, headwidth=5, label='Normal Vector', pivot='middle')  # Slightly thicker vector

# Plot the direction vector starting from the point on the line (flipped)
plt.quiver(x_vector_point, y_vector_point, direction_vector_scaled[0], direction_vector_scaled[1], color='forestgreen', angles='xy', scale_units='xy', scale=1,
           width=0.01, headwidth=5, label='Direction Vector', pivot='middle')  # Slightly thicker vector

# Set limits centered around the point of interest with ±5 range
plt.xlim(15, 25)  # Tightened x-axis limits
plt.ylim(y_vector_point - 5, y_vector_point + 5)  # Tightened y-axis limits to ±5 around the intersection point
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.title('Normal and Direction Vectors on the Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

