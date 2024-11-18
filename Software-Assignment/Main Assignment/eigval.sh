#!/bin/bash

# Check if input file is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <input_matrix_file>"
    exit 1
fi

INPUT_FILE=$1
BASENAME=$(basename "$INPUT_FILE" .txt)
OUTPUT_FILE="OutPut/OP${BASENAME//[!0-9]/}.txt"
LOG_FILE="Compile_Log/Log${BASENAME//[!0-9]/}.txt"

# Check if the input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Input file '$INPUT_FILE' not found!"
    exit 1
fi

# Create the output and log files if they don't exist
touch "$OUTPUT_FILE"
touch "$LOG_FILE"

# Read the matrix from the file
declare -a MATRIX
ROWS=$(head -n 1 "$INPUT_FILE")
COLS=$ROWS
count=0

# Read the matrix values
while read -r line; do
    if [ $count -gt 0 ]; then
        MATRIX+=($line)
    fi
    ((count++))
done < "$INPUT_FILE"

# Function to check if the matrix is symmetric
is_symmetric() {
    for ((i = 0; i < $ROWS; i++)); do
        for ((j = i + 1; j < $COLS; j++)); do
            # Check if matrix[i][j] equals matrix[j][i]
            if [[ ${MATRIX[$((i * $ROWS + j))]} != ${MATRIX[$((j * $ROWS + i))]} ]]; then
                return 1
            fi
        done
    done
    return 0
}

# Compile the code
echo "Compiling C code..."
gcc -o eigenvalues eigenvalues.c -lm

# If the matrix is symmetric, use the Jacobi method
if is_symmetric; then
    echo "Matrix is symmetric. Using Jacobi method..."
    gcc -o jacobi_method jacobi_method.c -lm
    ./jacobi_method "$INPUT_FILE" "$OUTPUT_FILE" "$LOG_FILE"
else
    echo "Matrix is not symmetric. Using QR method..."
    ./eigenvalues "$INPUT_FILE" "$OUTPUT_FILE" "$LOG_FILE"
fi

