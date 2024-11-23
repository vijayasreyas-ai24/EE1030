# Overview of File and Folder structure

This is an overview of the folder structure.

## Eigenvalue Algorithms
This includes the programs for algorithms unused in the assignment, but mentioned in the report.

## Main Assignment
Holds the main part of the Assignment, the program.
### TestCases
This is where the input files are stored as TC<case-number>.txt. There currently are 2 files in there, acting as an example.

### OutPut
This is where the computed eigenvalues are stored as OP<case-number>.txt.

### Compile_Log
This is for any additional prints like iterations, originally made for debugging purposes.

* <complex_utils.h> is a custom library, to try to reduce number of lines of code in the main programs themselves.
* <eigenvalues.c> and <jacobi_method.c> are the main c functions.
* We only run <eigval.sh>, it compiles the c codes, and checks the symmetry of the input matrices.

## Report
Self-Explanatory.