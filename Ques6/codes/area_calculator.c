#include <stdio.h>
#include <math.h>

// Function to calculate the area between the curve and the line
double area_enclosed(double* intersection_points) {
    // Limits of integration
    double x1 = -2.0;
    double x2 = 4.0;

    // Area calculation using the trapezoidal rule
    double area = 0.0;
    int n = 1000; // Number of intervals
    double dx = (x2 - x1) / n;

    for (int i = 0; i < n; i++) {
        double x_left = x1 + i * dx;
        double x_right = x1 + (i + 1) * dx;

        // Curve: y = (3/4)x^2
        double y_curve_left = (3.0 / 4.0) * x_left * x_left;
        double y_curve_right = (3.0 / 4.0) * x_right * x_right;

        // Line: y = (3/2)x + 6
        double y_line_left = (3.0 / 2.0) * x_left + 6;
        double y_line_right = (3.0 / 2.0) * x_right + 6;

        // Area of the trapezoid
        double area_left = (y_line_left - y_curve_left) * dx;
        double area_right = (y_line_right - y_curve_right) * dx;

        area += (area_left + area_right) / 2.0; // Average of left and right
    }

    // Calculate points of intersection
    intersection_points[0] = -2.0; // First intersection point
    intersection_points[1] = (3.0 / 2.0) * intersection_points[0] + 6; // y-value for first intersection

    intersection_points[2] = 4.0;  // Second intersection point
    intersection_points[3] = (3.0 / 2.0) * intersection_points[2] + 6; // y-value for second intersection

    return area;
}

int main() {
    double intersection_points[4]; // [x1, y1, x2, y2]
    double area = area_enclosed(intersection_points);
    
    // Output the area and intersection points
    printf("%.2f\n", area);  // Output the area
    printf("%.2f %.2f\n", intersection_points[0], intersection_points[1]); // First intersection
    printf("%.2f %.2f\n", intersection_points[2], intersection_points[3]); // Second intersection

    return 0;
}

