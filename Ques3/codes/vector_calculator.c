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

    // Print points on the line (y = (2/3)x + 2)
    for (int x = -5; x <= 5; x++) {
        double y = (2.0 / 3.0) * x + 2;  // Rearranged line equation
        printf("Line Point: [%d, %.2f]\n", x, y);
    }

    return 0;
}

