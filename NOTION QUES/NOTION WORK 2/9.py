'''### 9. Sort Strings Based on Length and Alphabet

👉 Sort list by length first, then lexicographically.

```python
Input: ["apple", "bat", "banana", "ant"]
Output: ["ant", "bat", "apple", "banana"]
```'''

a = ["apple","bat","banana","ant"]
c = []

for i in a:
    b=len(i)
    c.append([b,i])
c.sort()
x=[]

for j in c:
    x.append(j[1])
print(x)