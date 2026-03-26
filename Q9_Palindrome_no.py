# n=int(input("Enter a number: "))
# temp=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if temp==rev:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")



# s="madam"
# if s==s[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

s=input("enter a string is  :")
rev=""
for i in s:
    rev=i+rev


if s==rev:
    print("palindrome  ")
else:
    print("not palindrome ")