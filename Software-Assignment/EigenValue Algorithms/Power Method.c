#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_ITERATIONS 100
#define TOLERANCE 1e-6

double* power_method(double** matrix, int n, int max_iter) {
    double* vector = malloc(n * sizeof(double));
    double* next_vector = malloc(n * sizeof(double));
    double eigenvalue = 0.0;
    
    // Initial random vector
    for (int i = 0; i < n; i++) {
        vector[i] = 1.0 / n;
    }
    
    for (int iter = 0; iter < max_iter; iter++) {
        // Matrix-vector multiplication
        for (int i = 0; i < n; i++) {
            next_vector[i] = 0.0;
            for (int j = 0; j < n; j++) {
                next_vector[i] += matrix[i][j] * vector[j];
            }
        }
        
        // Normalize vector
        double norm = 0.0;
        for (int i = 0; i < n; i++) {
            norm += next_vector[i] * next_vector[i];
        }
        norm = sqrt(norm);
        
        for (int i = 0; i < n; i++) {
            next_vector[i] /= norm;
        }
        
        // Rayleigh quotient for eigenvalue estimation
        double new_eigenvalue = 0.0;
        for (int i = 0; i < n; i++) {
            double temp = 0.0;
            for (int j = 0; j < n; j++) {
                temp += matrix[i][j] * next_vector[j];
            }
            new_eigenvalue += temp * next_vector[i];
        }
        
        // Convergence check
        if (fabs(new_eigenvalue - eigenvalue) < TOLERANCE) {
            break;
        }
        
        eigenvalue = new_eigenvalue;
        
        // Swap vectors
        double* temp = vector;
        vector = next_vector;
        next_vector = temp;
    }
    
    // Return eigenvalue and dominant eigenvector
    double* result = malloc((n + 1) * sizeof(double));
    result[0] = eigenvalue;
    for (int i = 0; i < n; i++) {
        result[i + 1] = vector[i];
    }
    
    free(vector);
    free(next_vector);
    
    return result;
}
