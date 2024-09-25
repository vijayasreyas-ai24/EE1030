import subprocess
import matplotlib.pyplot as plt

# Call the C program and capture its output
result = subprocess.run(['./vector_calculator'], capture_output=True, text=True)

# Process the output
lines = result.stdout.strip().split('\n')
normal_vector = eval(lines[0].strip().split(': ')[1])
direction_vector = eval(lines[1].strip().split(': ')[1])

# Extract line points from the single output line
line_points_str = lines[2].strip().split(': ')[1]
line_points = eval('[' + line_points_str + ']')  # Convert string to list of tuples

# Separate line points into x and y coordinates
x_line, y_line = zip(*line_points)

# Set the new origin for the vectors at (0, 2)
shifted_origin = [0, 2]

# Create the plot
plt.quiver(*shifted_origin, *normal_vector, color='r', angles='xy', scale_units='xy', scale=1, 
           width=0.01, headwidth=5, label='Normal Vector', pivot='middle')
plt.quiver(*shifted_origin, *direction_vector, color='b', angles='xy', scale_units='xy', scale=1, 
           width=0.01, headwidth=5, label='Direction Vector', pivot='middle')

# Plot the original line
plt.plot(x_line, y_line, 'k--', label='Original Line (-2x + 3y = 6)', alpha=0.5)  # Dashed line

# Set limits and labels
plt.xlim(-5, 5)  # Adjust limits if necessary
plt.ylim(-5, 5)  # Adjust limits if necessary

# Ensure all important features are visible
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.title('Normal and Direction Vectors Starting from (0, 2)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

