#include <stdio.h>
#include <math.h>

int main() {
    // Fixed coordinates for points A and O
    double x1 = 3.0, y1 = -10.0;
    double x2 = 2.0, y2 = -3.0;
    double x3, y3;
    double radius;

   x3 = 2 * x2 - x1;
   y3 = 2 * y2 - y1;

   radius = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));

    // Output coordinates of points A, O, B, and the radius
    printf("%lf %lf\n", x1, y1);  // Point A
    printf("%lf %lf\n", x2, y2);  // Point O
    printf("%lf %lf\n", x3, y3);  // Point B
    printf("%lf\n", radius);      // Radius

    return 0;
}

