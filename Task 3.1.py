a=int(input("Enter the Number:- "))
def factorial(n):
    if n <2:
        return 1
    else:
        return n * (factorial(n-1))
b=factorial(a)
print("The factorial of",a,"is",b)
