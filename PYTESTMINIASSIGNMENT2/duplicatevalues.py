from collections import Counter
print("Return all the duplicate values from list of arraylist: ")
arr = [ [1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4] ]
for i in arr:
    d=dict(Counter(i))
    for j in d:
        if d[j]>1:
            print(j,"->",d[j],end=" ")
    print()
print()
