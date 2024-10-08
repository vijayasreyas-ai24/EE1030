import subprocess
import numpy as np
import matplotlib.pyplot as plt

# Compile the C code (make sure you have the C code in a file named circle.c)
subprocess.run(["gcc", "circle.c", "-o", "circle", "-lm"])

# Run the compiled C program and capture the output
result = subprocess.run(["./circle"], capture_output=True, text=True)

# Check for any errors in the execution of the C program
if result.returncode != 0:
    print("Error running the C program:")
    print(result.stderr)  # Print any error messages
else:
    # Split the output into lines
    output_lines = result.stdout.strip().split('\n')

    # Get the coordinates for points P and C
    point_P = np.array(list(map(float, output_lines[0].split()[1:])))  # P coordinates
    point_C = np.array(list(map(float, output_lines[1].split()[1:])))  # C coordinates

    # Get the circle points
    data = np.array(np.vstack(list(map(lambda line: np.fromstring(line, sep=' '), output_lines[2:]))))

    # Separate the circle points into x and y coordinates
    xp, yp = data[:, 0], data[:, 1]

    # Prepare for plotting
    plt.figure(figsize=(8, 8))

    # Plot the discrete circle points with smaller size
    plt.scatter(xp, yp, color='k', marker='o', s=5)  # Smaller discrete circle points
    plt.scatter(point_C[0], point_C[1], color='forestgreen', marker='o', s=60, label=f'C {point_C}')  # Center point (C)
    plt.scatter(point_P[0], point_P[1], color='navy', marker='o', s=60, label=f'P {point_P}')  # Point (P)

    # Label the points to the right
    plt.text(point_C[0] + 0.3, point_C[1], f'C {point_C}', fontsize=9, ha='left')
    plt.text(point_P[0] + 0.3, point_P[1], f'P {point_P}', fontsize=9, ha='left')

    plt.title('Circle and Points involved')  # Updated title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Set graph limits to ensure all points are visible
    plt.xlim(-4, 10)  # X-axis limits
    plt.ylim(-2, 12)  # Y-axis limits

    # Add gridlines for both odd and even integers
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(-4, 11, 1))  # Set x ticks for odd and even integers
    plt.yticks(np.arange(-2, 13, 1))  # Set y ticks for odd and even integers

    plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio
    plt.axhline(0, color='grey', lw=0.5)
    plt.axvline(0, color='grey', lw=0.5)
    plt.legend()
    plt.show()
    
