l=[1,2,3,4,3,2,1]
new_list=[]
for i in l:
    if i not in new_list:
        new_list.append(i)
print("Elemnets are",new_list)