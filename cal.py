# Hardcoded values (Static variables)
a = 20
b = 4

# Operation Functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error"

# Execution
print("Results:")
print(f"Add:      {add(a, b)}")
print(f"Subtract: {subtract(a, b)}")
print(f"Multiply: {multiply(a, b)}")

print(f"Divide:   {divide(a, b)}")



pipeline {
    agent any 

    stages {
        stage('Setup File') {
            steps {
                echo 'Creating the Python script...'
                // These lines write the Python code directly into the workspace
                bat 'echo a = 20 > calculator.py'
                bat 'echo b = 4 >> calculator.py'
                bat 'echo def add(x, y): return x + y >> calculator.py'
                bat 'echo def subtract(x, y): return x - y >> calculator.py'
                bat 'echo def multiply(x, y): return x * y >> calculator.py'
                bat 'echo def divide(x, y): return x / y if y != 0 else "Error" >> calculator.py'
                bat 'echo print(f"Add: {add(a, b)}") >> calculator.py'
                bat 'echo print(f"Subtract: {subtract(a, b)}") >> calculator.py'
                bat 'echo print(f"Multiply: {multiply(a, b)}") >> calculator.py'
                bat 'echo print(f"Divide: {divide(a, b)}") >> calculator.py'
            }
        }
        stage('Static Analysis') {
            steps {
                echo 'Checking syntax...'
                bat 'python -m py_compile calculator.py'
            }
        }
        stage('Run Calculator') {
            steps {
                echo 'Executing Results...'
                bat 'python calculator.py'
            }
        }
    }
}
