input1 = input("Enter anything 1: ")
input2 = input("Enter anything 2: ")

try:
    int(input1)
except ValueError:
    print("Input 1 is a string.")
else:
    print("Input 1 is an integer.")

try:
    int(input2)
except ValueError:
    print("Input 2 is a string.")
else:
    print("Input 2 is an integer.")
