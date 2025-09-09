import math

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

n= int(input("Enter the number: "))
result=factorial(n)
print(f"Factorial of {n} is: ", result)


#--------------------------

x=int(input("Enter the number: "))

print("Square root: ", math.sqrt(x))
print("Logarithm: ", math.log(x))
print("Sine: ", math.sin(x))


