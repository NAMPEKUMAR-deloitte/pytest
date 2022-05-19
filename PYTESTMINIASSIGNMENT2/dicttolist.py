print("Convert Dictionary to list: ")
dict1={"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
temp=[]
j=0
for i in dict1:
    temp.append(dict1[i])
    temp[j].insert(0,i)
    j+=1
print(temp)
