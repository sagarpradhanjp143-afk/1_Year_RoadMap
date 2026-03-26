l=[23,45,56,65,34,45]
largest=l[0]
second_largest=l[0]
for i in l:
    if i>largest:
        second_largest=largest
        largest=i
    elif i >second_largest and i!=largest:
        second_largest=i
print("Second largest is :",second_largest)

