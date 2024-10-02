import subprocess
import numpy as np
import matplotlib.pyplot as plt

# Call the C program and capture the output
def run_c_program():
    result = subprocess.run(['./area_calculator'], stdout=subprocess.PIPE, text=True)
    output = result.stdout.strip().split('\n')
    area = float(output[0])
    intersections = [tuple(map(float, line.split())) for line in output[1:]]
    return area, intersections

# Get the area and intersection points from the C program
area, intersections = run_c_program()

# Define the functions using vectorized operations
def curve(x):
    return (3 / 4) * x**2

def line(x):
    return (3 / 2) * x + 6

# Generate x values
x_values = np.linspace(-3, 5, 400)
curve_values = curve(x_values)
line_values = line(x_values)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_values, curve_values, label=r'$y = \frac{3}{4}x^2$', color='darkblue')  # Dark Blue for the curve
plt.plot(x_values, line_values, label=r'$y = \frac{3}{2}x + 6$', color='limegreen')  # Lime Green for the line

# Fill the area between the curves
plt.fill_between(x_values, curve_values, line_values, 
                 where=(x_values >= -2) & (x_values <= 4), 
                 color='mediumturquoise', alpha=0.2)  # Medium Turquoise for shaded region

# Plot intersection points
for x, y in intersections:
    plt.plot(x, y, 'o', color='teal')  # Mark intersection points
    plt.text(x, y, f'({x:.1f}, {y:.1f})', fontsize=10, color='teal', ha='right')  # Label intersection points

# Setting the labels and title
plt.title('Area Enclosed Between the Curve and the Line')  # Updated title
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.xlim(-3, 5)
plt.ylim(-5, 15)

# Show the plot
plt.show()

