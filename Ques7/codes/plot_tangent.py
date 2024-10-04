import subprocess
import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

# Compile the C program and check for errors
compile_process = subprocess.run(["gcc", "tangent.c", "-o", "tangent", "-lm"], capture_output=True, text=True)
if compile_process.returncode != 0:
    print("Compilation error:")
    print(compile_process.stderr)
    exit(1)

# Run the C program
result = subprocess.run(["./tangent"], capture_output=True, text=True)

# Check for execution errors
if result.returncode != 0:
    print("Execution error:")
    print(result.stderr)
    exit(1)

# Extract point of tangency and tangent line from the output
output_lines = result.stdout.splitlines()
if len(output_lines) < 2:
    print("Unexpected output from the C program.")
    print(result.stdout)
    exit(1)

# Parse output
point_line = output_lines[0].split(": ")[1]
tangent_line = output_lines[1].split(": ")[1]

# Extract x and y coordinates of the point of tangency
x_tangent, y_tangent = map(float, point_line.strip("()").split(", "))

# Set specific coordinates for the point of tangency
x_tangent_frac = Fraction(41, 48)
y_tangent_frac = Fraction(3, 4)

# Extract slope and intercept of the tangent line
slope, intercept = map(float, tangent_line.split(" = ")[1].split("x + "))

# Create x values for the curve
x_curve = np.linspace(0.67, 11, 400)  # Start just above 2/3 to avoid NaN values
y_curve = np.sqrt(3 * x_curve - 2)

# Create x values for the tangent line and original line across a wider range
x_full = np.linspace(-1, 11, 400)  # Extend the x values for full coverage
y_tangent_line = slope * x_full + (y_tangent - slope * x_tangent)
y_original_line = 2 * x_full + 2.5  # Original line: y = 2x + 2.5

# Prepare the tangent line label with a fraction
intercept_fraction = Fraction(intercept).limit_denominator()
if intercept_fraction.denominator == 1:
    tangent_label = f"Tangent Line: $y = {slope:.0f}x - {abs(intercept_fraction.numerator)}$"
else:
    tangent_label = f"Tangent Line: $y = {slope:.0f}x - \\frac{{{abs(intercept_fraction.numerator)}}}{{{intercept_fraction.denominator}}}$"

# Create the plot
plt.figure(figsize=(12, 8))  # Increased figure size for better visibility
plt.plot(x_curve, y_curve, label='Curve: $y = \\sqrt{3x - 2}$', color='navy')
plt.plot(x_full, y_tangent_line, label=tangent_label, color='forestgreen', linestyle='--')
plt.plot(x_full, y_original_line, label='Original Line: $4x - 2y + 5 = 0$', color='black', linestyle='-')
plt.scatter(float(x_tangent_frac), float(y_tangent_frac), color='lightseagreen', label='Point of Tangency', zorder=5)

# Label the point of tangency with specified coordinates
plt.text(float(x_tangent_frac) - 0.5, float(y_tangent_frac) + 0.1, f'({x_tangent_frac}, {y_tangent_frac})', fontsize=10, color='black')

plt.title('Tangent to the Curve and Original Line')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.xlim(-1, 11)  # Set x-axis limit
plt.ylim(-1, 11)  # Set y-axis limit
plt.grid()
plt.legend()
plt.show()

