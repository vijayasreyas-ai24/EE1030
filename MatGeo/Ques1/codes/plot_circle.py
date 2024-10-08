import matplotlib.pyplot as plt
import subprocess

# Function to plot the circle
def plot_circle(ax, center, radius, **kwargs):
    circle = plt.Circle(center, radius, edgecolor='black', facecolor='none', **kwargs)
    ax.add_artist(circle)

# Function to plot a line between two points
def plot_line(ax, point1, point2, **kwargs):
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    ax.plot(x_values, y_values, **kwargs)

def main():
    # Run the C code and capture its output
    result = subprocess.run(['./compute_b'], capture_output=True, text=True)
    output = result.stdout.splitlines()

    # Parse the coordinates and radius from the output
    x1, y1 = map(float, output[0].strip().split())
    x2, y2 = map(float, output[1].strip().split())
    x3, y3 = map(float, output[2].strip().split())
    radius = float(output[3].strip())

    # Plotting
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Plot diameter AB (lighter color)
    plot_line(ax, (x1, y1), (x3, y3), color='lightblue', linestyle='-', linewidth=2)

    # Plot circle with a solid boundary (no fill)
    plot_circle(ax, (x2, y2), radius, linestyle='-', linewidth=2)

    # Plot points A, O, B
    ax.plot([x1], [y1], 'bo', label='Point A')  # Point A
    ax.plot([x2], [y2], 'ko', label='Point O')  # Point O
    ax.plot([x3], [y3], 'bo', label='Point B')  # Point B

    # Calculate limits to ensure the circle is fully visible
    x_center, y_center = x2, y2
    ax.set_xlim(x_center - radius - 1, x_center + radius + 1)
    ax.set_ylim(y_center - radius - 1, y_center + radius + 1)

    # Add labels and legend with coordinates
    ax.text(x1, y1, f' A ({x1:.2f}, {y1:.2f})', fontsize=12, verticalalignment='bottom', color='blue')
    ax.text(x2, y2, f' O ({x2:.2f}, {y2:.2f})', fontsize=12, verticalalignment='bottom', color='black')
    ax.text(x3, y3, f' B ({x3:.2f}, {y3:.2f})', fontsize=12, verticalalignment='bottom', color='blue')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.grid(True)
    
    plt.title('Circle with Diameter AB')
    plt.show()

if __name__ == "__main__":
    main()

