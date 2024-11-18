#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include "complex_utils.h"

#define MAX_ITERATIONS 1000
#define EPSILON 1e-12

void complex_print_matrix(Complex** A, int n);
void complex_jacobi_rotation(Complex** A, int n, int p, int q);
void complex_jacobi_method(Complex** A, int n, Complex* eigenvalues);

int main(int argc, char* argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s <input_matrix_file> <output_file> <log_file>\n", argv[0]);
        return 1;
    }

    FILE* inputFile = fopen(argv[1], "r");
    FILE* outputFile = fopen(argv[2], "w");
    FILE* logFile = fopen(argv[3], "w");

    if (!inputFile || !outputFile || !logFile) {
        fprintf(stderr, "Error opening files\n");
        return 1;
    }

    int n;
    fscanf(inputFile, "%d", &n);
    
    Complex** A = malloc(n * sizeof(Complex*));
    for (int i = 0; i < n; i++) {
        A[i] = malloc(n * sizeof(Complex));
    }

    // Read matrix with comma-separated complex entries
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            char entry[50];
            double real, imag = 0.0;
            fscanf(inputFile, "%s", entry);
            
            char *comma = strchr(entry, ',');
            if (comma) {
                *comma = '\0';
                real = atof(entry);
                imag = atof(comma + 1);
            } else {
                real = atof(entry);
            }
            
            A[i][j].real = real;
            A[i][j].imag = imag;
        }
    }

    Complex* eigenvalues = malloc(n * sizeof(Complex));
    complex_jacobi_method(A, n, eigenvalues);

    // Write complex eigenvalues
    for (int i = 0; i < n; i++) {
        complex_print(eigenvalues[i], outputFile);
        fprintf(outputFile, "\n");
    }

    // Free memory
    for (int i = 0; i < n; i++) {
        free(A[i]);
    }
    free(A);
    free(eigenvalues);

    fclose(inputFile);
    fclose(outputFile);
    fclose(logFile);

    return 0;
}

void complex_print_matrix(Complex** A, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            complex_print(A[i][j], stdout);
            printf(" ");
        }
        printf("\n");
    }
}

void complex_jacobi_rotation(Complex** A, int n, int p, int q) {
    Complex theta = {0, 0};
    Complex t = {0, 0}, c = {0, 0}, s = {0, 0};

    // Note: This is a simplified version. Full complex Jacobi rotation is more intricate
    if (complex_magnitude(A[p][q]) > EPSILON) {
        // Compute rotation parameters
        theta.real = 0.5 * atan2(2 * A[p][q].real, A[q][q].real - A[p][p].real);
        t.real = tan(theta.real);
        
        c.real = 1 / sqrt(1 + t.real * t.real);
        s.real = t.real * c.real;

        // Modify matrix columns
        for (int i = 0; i < n; i++) {
            Complex temp1 = A[i][p];
            Complex temp2 = A[i][q];
            
            A[i][p].real = c.real * temp1.real - s.real * temp2.real;
            A[i][p].imag = c.real * temp1.imag - s.real * temp2.imag;
            
            A[i][q].real = s.real * temp1.real + c.real * temp2.real;
            A[i][q].imag = s.real * temp1.imag + c.real * temp2.imag;
        }

        // Modify matrix rows
        for (int i = 0; i < n; i++) {
            Complex temp1 = A[p][i];
            Complex temp2 = A[q][i];
            
            A[p][i].real = c.real * temp1.real - s.real * temp2.real;
            A[p][i].imag = c.real * temp1.imag - s.real * temp2.imag;
            
            A[q][i].real = s.real * temp1.real + c.real * temp2.real;
            A[q][i].imag = s.real * temp1.imag + c.real * temp2.imag;
        }

        // Update diagonal
