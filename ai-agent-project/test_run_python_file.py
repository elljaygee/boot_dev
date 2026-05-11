from functions.run_python_file import run_python_file


print("Result for current directory:")
print(run_python_file("calculator", "main.py"))

print("Result for current directory:")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("Result for current directory:")
print(run_python_file("calculator", "tests.py"))

print("Result for current directory:")
print(run_python_file("calculator", "../main.py"))

print("Result for current directory:")
print(run_python_file("calculator", "nonexistent.py"))

print("Result for current directory:")
print(run_python_file("calculator", "lorem.txt"))