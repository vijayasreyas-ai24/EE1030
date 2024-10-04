#include <stdio.h>
#include <math.h>

// Function representing the curve
double f(double x) {
    return sqrt(3 * x - 2);
}

// Derivative of the curve
double df(double x) {
    return 1.5 / sqrt(3 * x - 2);
}

int main() {
    double slope = 2.0; // Slope of the given line 4x - 2y + 5 = 0
    double x_tangent, y_tangent;

    // Solve for x where df(x) = slope
    x_tangent = ((1.5 / slope) * (1.5 / slope) + 2) / 3.0;
    y_tangent = f(x_tangent);
    
    // Print the point of tangency and the tangent line
    printf("Point of Tangency: (%.2f, %.2f)\n", x_tangent, y_tangent);
    printf("Tangent Line: y = %.2fx + %.2f\n", slope, y_tangent - slope * x_tangent);
    
    return 0;
}

