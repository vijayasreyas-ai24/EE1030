#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>
#include <string.h>
#include "complex_utils.h"

#define MAX_ITER 1000
#define TOLERANCE 1e-6

void complex_qr_decomposition(Complex *A, Complex *Q, Complex *R, int n);
void complex_multiply_matrices(Complex *A, Complex *B, Complex *C, int n);
void complex_qr_shift_algorithm(Complex *A, Complex *eigenvalues, int n, FILE *logfile);

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s <input_file> <output_file> <log_file>\n", argv[0]);
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");
    FILE *output_file = fopen(argv[2], "w");
    FILE *log_file = fopen(argv[3], "w");

    if (!input_file || !output_file || !log_file) {
        fprintf(stderr, "Error opening files\n");
        return 1;
    }

    int n;
    fscanf(input_file, "%d", &n);

    Complex *A = malloc(n * n * sizeof(Complex));
    Complex *eigenvalues = malloc(n * sizeof(Complex));

    // Read matrix with comma-separated complex entries
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            char entry[50];
            double real, imag = 0.0;
            fscanf(input_file, "%s", entry);
            
            // Check if comma-separated
            char *comma = strchr(entry, ',');
            if (comma) {
                *comma = '\0';
                real = atof(entry);
                imag = atof(comma + 1);
            } else {
                real = atof(entry);
            }
            
            A[i * n + j].real = real;
            A[i * n + j].imag = imag;
        }
    }

    complex_qr_shift_algorithm(A, eigenvalues, n, log_file);

    // Write complex eigenvalues
    for (int i = 0; i < n; i++) {
        complex_print(eigenvalues[i], output_file);
        fprintf(output_file, "\n");
    }

    free(A);
    free(eigenvalues);
    fclose(input_file);
    fclose(output_file);
    fclose(log_file);

    return 0;
}

void complex_qr_decomposition(Complex *A, Complex *Q, Complex *R, int n) {
    // Similar to real matrix QR, but with complex matrix operations
    for (int i = 0; i < n * n; i++) {
        Q[i].real = 0.0;
        Q[i].imag = 0.0;
        R[i].real = 0.0;
        R[i].imag = 0.0;
    }

    for (int i = 0; i < n; i++) {
        // Gram-Schmidt process with complex inner products
        for (int j = 0; j < i; j++) {
            Complex dot_product = {0, 0};
            for (int k = 0; k < n; k++) {
                Complex conj_col = complex_conjugate(Q[k * n + j]);
                dot_product = complex_add(dot_product, 
                    complex_multiply(A[k * n + i], conj_col));
            }
            R[j * n + i] = dot_product;

            for (int k = 0; k < n; k++) {
                Complex scaled = complex_multiply(dot_product, Q[k * n + j]);
                A[k * n + i] = complex_subtract(A[k * n + i], scaled);
            }
        }

        // Normalize the column
        Complex norm_sq = {0, 0};
        for (int k = 0; k < n; k++) {
            norm_sq = complex_add(norm_sq, 
                complex_multiply(A[k * n + i], complex_conjugate(A[k * n + i])));
        }
        double norm = sqrt(norm_sq.real);
        R[i * n + i].real = norm;

        for (int k = 0; k < n; k++) {
            Q[k * n + i].real = A[k * n + i].real / norm;
            Q[k * n + i].imag = A[k * n + i].imag / norm;
        }
    }
}

void complex_multiply_matrices(Complex *A, Complex *B, Complex *C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i * n + j].real = 0.0;
            C[i * n + j].imag = 0.0;
            for (int k = 0; k < n; k++) {
                Complex product = complex_multiply(A[i * n + k], B[k * n + j]);
                C[i * n + j] = complex_add(C[i * n + j], product);
            }
        }
    }
}

void complex_qr_shift_algorithm(Complex *A, Complex *eigenvalues, int n, FILE *logfile) {
    Complex *Q = malloc(n * n * sizeof(Complex));
    Complex *R = malloc(n * n * sizeof(Complex));
    Complex *A_new = malloc(n * n * sizeof(Complex));

    Complex shift = {0, 0};

    for (int iter = 0; iter < MAX_ITER; iter++) {
        // Similar shift strategy, but using complex numbers
        Complex last_diagonal = A[(n-1) * n + (n-1)];
        Complex prev_diagonal = A[(n-2) * n + (n-2)];
        Complex off_diagonal = A[(n-2) * n + (n-1)];

        shift.real = (last_diagonal.real + prev_diagonal.real) / 2.0;
        shift.imag = (last_diagonal.imag + prev_diagonal.imag) / 2.0;

        // Subtract shift from diagonal
        for (int i = 0; i < n; i++) {
            A[i * n + i] = complex_subtract(A[i * n + i], shift);
        }

        complex_qr_decomposition(A, Q, R, n);
        complex_multiply_matrices(R, Q, A_new, n);

        // Add shift back
        for (int i = 0; i < n; i++) {
            A_new[i * n + i] = complex_add(A_new[i * n + i], shift);
        }

        memcpy(A, A_new, n * n * sizeof(Complex));

        // Convergence check (magnitude of off-diagonal elements)
        double off_diagonal_norm = 0.0;
        for (int i = 0; i < n - 1; i++) {
            off_diagonal_norm += complex_magnitude(A[i * n + (i+1)]);
        }

        if (off_diagonal_norm < TOLERANCE) break;
    }

    // Extract eigenvalues
    for (int i = 0; i < n; i++) {
        eigenvalues[i] = A[i * n + i];
    }

    free(Q);
    free(R);
    free(A_new);
}
