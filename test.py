num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

# Iterate through numbers from 1 to 100
for i in range(1, 101):
    if i % num1 == 0 and i % num2 == 0:
        print("Howdy Whoop")
    elif i % num1 == 0:
        print("Howdy")
    elif i % num2 == 0:
        print("Whoop")
    else:
        print(i)