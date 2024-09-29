#include <stdio.h>
#include <math.h>

#define NUM_POINTS 300 // Number of points on the circle

void calculateCirclePoints(double xc, double yc, double radius) {
    for (int i = 0; i < NUM_POINTS; i++) {
        double angle = 2 * M_PI * i / NUM_POINTS; // Angle in radians
        double xp = xc + radius * cos(angle); // xp coordinate
        double yp = yc + radius * sin(angle); // yp coordinate
        printf("%.2f %.2f\n", xp, yp); // Print circle points
    }
}

int main() {
    // Pre-defined center coordinates and radius
    double xc = 3.0; // Center x-coordinate
    double yc = 5.0; // Center y-coordinate
    double radius = 6.0; // Radius

    // Pre-defined point P coordinates
    double xp = -2.0; // Point P x-coordinate
    double yp = 4.0;  // Point P y-coordinate

    // Print point P
    printf("P %.2f %.2f\n", xp, yp);

    // Print center C
    printf("C %.2f %.2f\n", xc, yc);

    // Calculate and print circle points
    calculateCirclePoints(xc, yc, radius);

    return 0;
}

