'''### 10. Find Most Frequent Word
Input: ["apple", "banana", "apple", "cherry"]
Output: "apple"

👉 Return the most occurring string in a list.'''


'''a=["apple","banana","apple","cherry"]

for i in a:
    a.count(i)'''

'''a=["apple", "banana", "apple", "cherry"]
for i in a :
    a.count(i)'''
a= ["apple", "banana", "apple", "cherry"]
b=[]
for i in a:
    if a.count(i)>1:
        a.remove(i)
        b.append(i)
print("".join(b))
