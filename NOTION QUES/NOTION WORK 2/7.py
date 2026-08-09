'''### 7. Find Common Characters in All Strings

👉 Return characters that appear in all words.

```python
Input: ["bella", "label", "roller"]
Output: ["e", "l"]
```'''

a = ["bella","label","roller"]

result = []

for j in a[0]:
    if j in a[1] and j in a[2]:
        result.append(j)
print(set(result))