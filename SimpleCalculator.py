

n1=int(input("Enter the number is :"))
n2=int(input("Enter the number is :"))

choice=input("Choice one number 1/2/3/4/5 ")

if choice=='1':
    print("Result :",n1+n2)
elif choice =='2':
    print("Result",n1-n2)
elif choice =='3':
    print("Result",n1*n2)
elif choice =='4':
    print("Result",n1/n2)
elif choice =='5':
    print("Result",n1%n2)

else:
    print("Invalid number")