#include <stdio.h>
#include <math.h>

// Function to compute point B
void compute_B(double x1, double y1, double x2, double y2, double *x3, double *y3) {
    *x3 = 2 * x2 - x1;
    *y3 = 2 * y2 - y1;
}

// Function to compute the radius of the circle
double compute_radius(double x1, double y1, double x3, double y3) {
    return sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1)) / 2;
}

int main() {
    // Fixed coordinates for points A and O
    double x1 = 3.0, y1 = -10.0;
    double x2 = 2.0, y2 = -3.0;
    double x3, y3;
    double radius;

    // Compute coordinates of point B
    compute_B(x1, y1, x2, y2, &x3, &y3);

    // Compute the radius of the circle
    radius = compute_radius(x1, y1, x3, y3);

    // Output coordinates of points A, O, B, and the radius
    printf("%lf %lf\n", x1, y1);  // Point A
    printf("%lf %lf\n", x2, y2);  // Point O
    printf("%lf %lf\n", x3, y3);  // Point B
    printf("%lf\n", radius);      // Radius

    return 0;
}

