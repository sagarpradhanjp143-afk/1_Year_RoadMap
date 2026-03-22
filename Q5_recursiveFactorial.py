
# def FactorialNumber(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# n=int(input("Enter the number is :"))
# result=FactorialNumber(n)
# print("Factorial of number is :",result)

def factorial(n):
    if n==0 or  n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number is :"))
print("Factorial number is :",factorial(n))

   

