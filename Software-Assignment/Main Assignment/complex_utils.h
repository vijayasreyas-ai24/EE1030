#ifndef COMPLEX_UTILS_H
#define COMPLEX_UTILS_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    double real;
    double imag;
} Complex;

Complex complex_add(Complex a, Complex b);
Complex complex_subtract(Complex a, Complex b);
Complex complex_multiply(Complex a, Complex b);
Complex complex_divide(Complex a, Complex b);
Complex complex_conjugate(Complex a);
double complex_magnitude(Complex a);
double complex_argument(Complex a);
void complex_print(Complex a, FILE* stream);

Complex complex_add(Complex a, Complex b) {
    Complex result = {a.real + b.real, a.imag + b.imag};
    return result;
}

Complex complex_subtract(Complex a, Complex b) {
    Complex result = {a.real - b.real, a.imag - b.imag};
    return result;
}

Complex complex_multiply(Complex a, Complex b) {
    Complex result = {
        a.real * b.real - a.imag * b.imag,
        a.real * b.imag + a.imag * b.real
    };
    return result;
}

Complex complex_divide(Complex a, Complex b) {
    double denominator = b.real * b.real + b.imag * b.imag;
    Complex result = {
        (a.real * b.real + a.imag * b.imag) / denominator,
        (a.imag * b.real - a.real * b.imag) / denominator
    };
    return result;
}

Complex complex_conjugate(Complex a) {
    Complex result = {a.real, -a.imag};
    return result;
}

double complex_magnitude(Complex a) {
    return sqrt(a.real * a.real + a.imag * a.imag);
}

double complex_argument(Complex a) {
    return atan2(a.imag, a.real);
}

void complex_print(Complex a, FILE* stream) {
    if (fabs(a.imag) < 1e-10) {
        // Essentially real number
        fprintf(stream, "%10.6f", a.real);
    } else if (a.imag >= 0) {
        fprintf(stream, "%10.6f+%10.6fi", a.real, a.imag);
    } else {
        fprintf(stream, "%10.6f%10.6fi", a.real, a.imag);
    }
}

#endif
