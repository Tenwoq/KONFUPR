import os

def run_tests():
    # Create a simple test program
    test_program = """
# Test Program
LOAD_CONST 41 10 5       # Initialize vector 1, element 1
LOAD_CONST 41 11 8       # Initialize vector 1, element 2
LOAD_CONST 41 20 4       # Initialize vector 2, element 1
LOAD_CONST 41 21 8       # Initialize vector 2, element 2
BINARY_OP 7 10 20 0      # Compare vector1[0] >= vector2[0]
BINARY_OP 7 11 21 0      # Compare vector1[1] >= vector2[1]
"""

    # Write test program to file
    with open("program.txt", "w") as f:
        f.write(test_program)

    print("Running Assembler...")
    os.system("python3 assembler.py")

    print("Running Interpreter...")
    os.system("python3 interpreter.py")

    print("Test completed. Check 'log.xml' and 'memory.xml' for results.")

if __name__ == "__main__":
    run_tests()
