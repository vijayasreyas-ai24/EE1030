#include <stdio.h>

int main() {
    // Coefficients of the line -2x + 3y = 6
    int A = -2;
    int B = 3;

    // Normal vector
    int normal_vector[2] = {A, B};

    // Direction vector (perpendicular to normal)
    int direction_vector[2] = {B, -A};  // Swapping and negating A

    // Print the vectors
    printf("Normal Vector: [%d, %d]\n", normal_vector[0], normal_vector[1]);
    printf("Direction Vector: [%d, %d]\n", direction_vector[0], direction_vector[1]);

    // Print all points on the line in a single line
    printf("Line Points: ");
    for (int x = -5; x <= 5; x++) {
        double y = (2.0 / 3.0) * x + 2;  // Rearranged line equation
        printf("[%d, %.2f]", x, y);
        if (x < 5) printf(", ");  // Add a comma between points, but not after the last point
    }
    printf("\n");

    return 0;
}

