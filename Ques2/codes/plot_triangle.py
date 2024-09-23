import subprocess
import matplotlib.pyplot as plt

# Call the C executable and capture the output without printing it to the terminal
result = subprocess.run(["./triangle"], capture_output=True, text=True)

# Parse the output
coordinates = {}
for line in result.stdout.splitlines():
    # Strip the colon from the name
    name, x, y = line.split()
    coordinates[name[:-1]] = (float(x), float(y))  # Remove the last character (colon)

# Check if coordinates contain expected keys
if 'A' not in coordinates or 'B' not in coordinates or 'C' not in coordinates:
    print("Error: Missing expected coordinates.")
    print("Available coordinates:", coordinates)
    exit(1)

# Unpack the coordinates
A = coordinates['A']
B = coordinates['B']
C = coordinates['C']

# Create a figure and axis with reduced size
plt.figure(figsize=(6, 6))  # Adjust the figure size as needed

# Plotting line segments with the specified colors
plt.plot([A[0], B[0]], [A[1], B[1]], color='forestgreen', label='AB')  # AB
plt.plot([A[0], C[0]], [A[1], C[1]], color='teal', label='AC')        # AC
plt.plot([B[0], C[0]], [B[1], C[1]], color='orangered', label='BC')   # BC

# Adding points A, B, C to the plot with colors matching the opposite segments
plt.scatter(*A, color='orangered', zorder=5)  # Point A matches BC
plt.scatter(*B, color='teal', zorder=5)       # Point B matches AC
plt.scatter(*C, color='forestgreen', zorder=5) # Point C matches AB

# Adding labels with coordinates
plt.text(A[0], A[1], f'A {A}', fontsize=12, ha='right', color='orangered')
plt.text(B[0], B[1], f'B {B}', fontsize=12, ha='right', color='teal')
plt.text(C[0], C[1], f'C {C}', fontsize=12, ha='left', color='forestgreen')

# Setting limits and labels
plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.title('Triangle ABC')
plt.grid()
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')

# Use tight layout to reduce excess whitespace
plt.tight_layout()

# Show the plot
plt.show()

