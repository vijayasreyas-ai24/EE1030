import subprocess
import matplotlib.pyplot as plt
import numpy as np
from sympy import Rational, sqrt, latex

# Compile and run the C program, capturing all outputs
result = subprocess.run(["gcc", "tangent.c", "-o", "tangent", "-lm"], capture_output=True, text=True)
if result.returncode != 0:
    print("Compilation error:")
    print(result.stderr)
    exit(1)

# Run the compiled C program
result = subprocess.run(["./tangent"], capture_output=True, text=True)

# Check for execution errors
if result.returncode != 0:
    print("Execution error:")
    print(result.stderr)
    exit(1)

# Extract point of tangency, tangent line, and normal line from the output
output_lines = result.stdout.splitlines()
if len(output_lines) < 3:
    print("Unexpected output from the C program.")
    print(result.stdout)
    exit(1)

# Parse output
point_line = output_lines[0].split(": ")[1]
tangent_line = output_lines[1].split(": ")[1]
normal_line = output_lines[2].split(": ")[1]

# Extract x and y coordinates of the point of tangency
x_tangent, y_tangent = map(float, point_line.strip("()").split(", "))

# Extract slope and intercept of the tangent line
slope_tangent, intercept_tangent = map(float, tangent_line.split(" = ")[1].split("x + "))
# Extract slope and intercept of the normal line
slope_normal, intercept_normal = map(float, normal_line.split(" = ")[1].split("x + "))

# Convert slopes and intercepts to fractions
slope_tangent_frac = Rational(slope_tangent).limit_denominator()
intercept_tangent_frac = Rational(intercept_tangent).limit_denominator()
slope_normal_frac = Rational(slope_normal).limit_denominator()
intercept_normal_frac = Rational(intercept_normal).limit_denominator()

# Create x values for the curve
x_curve = np.linspace(0.67, 11, 400)  # Avoid NaN values
y_curve = np.sqrt(3 * x_curve - 2)

# Create x values for the tangent line, normal line, and original line
x_full = np.linspace(-1, 11, 400)
y_tangent_line = slope_tangent * x_full + (y_tangent - slope_tangent * x_tangent)
y_normal_line = slope_normal * x_full + intercept_normal
y_original_line = 2 * x_full + 2.5  # Original line: y = 2x + 2.5

# Create the plot
plt.figure(figsize=(12, 8))
plt.plot(x_curve, y_curve, label='Curve: $y = \\sqrt{3x - 2}$', color='navy')
plt.plot(x_full, y_tangent_line, label=f'Tangent Line: $y = {latex(slope_tangent_frac)}x + {latex(intercept_tangent_frac)}$', color='forestgreen', linestyle='--')
plt.plot(x_full, y_normal_line, label=f'Normal Line: $y = {latex(slope_normal_frac)}x + {latex(intercept_normal_frac)}$', color='crimson', linestyle='--')
plt.plot(x_full, y_original_line, label='Original Line: $4x - 2y + 5 = 0$', color='black', linestyle='-')
plt.scatter(x_tangent, y_tangent, color='lightseagreen', label='Point of Tangency', zorder=5)

# Label the point of tangency
plt.text(x_tangent - 0.5, y_tangent + 0.1, f'({x_tangent:.2f}, {y_tangent:.2f})', fontsize=10, color='black')

plt.title('Tangent and Normal to the Curve with Original Line')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.xlim(-1, 11)
plt.ylim(-1, 11)
plt.grid()
plt.legend()
plt.show()

