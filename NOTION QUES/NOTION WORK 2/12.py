'''### 12. Check Palindrome Strings in List

👉 Return all palindrome words.

```python
Input: ["madam", "hello", "racecar"]
Output: ["madam", "racecar"]
```'''

a = ["madam","hello","racecar"]
b=[]

for i in a:
    if i == i[::-1]:
        b.append(i)
print(b)