#include <stdio.h>
#include <math.h>

int main() {
    // Given values
    double CA = 6.0;          // Side CA
    double AB = 5.0;          // Side AB
    double angle_BAC = 45.0;  // Angle BAC in degrees

    // Convert angle from degrees to radians
    double angle_BAC_rad = angle_BAC * (M_PI / 180.0);

    // Coordinates
    double B[2] = {0.0, 0.0};  // Point B at the origin
    double C[2] = {CA, 0.0};   // Point C on the x-axis
    double A[2];               // Point A to be calculated

    // Calculate coordinates of Point A in the first quadrant
    A[0] = AB * cos(angle_BAC_rad);  // x-coordinate of A
    A[1] = AB * sin(angle_BAC_rad);  // y-coordinate of A

    // Output coordinates to standard output
    printf("A: %.2f %.2f\n", A[0], A[1]);
    printf("B: %.2f %.2f\n", B[0], B[1]);
    printf("C: %.2f %.2f\n", C[0], C[1]);

    return 0;
}

