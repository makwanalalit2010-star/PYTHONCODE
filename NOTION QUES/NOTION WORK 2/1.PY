'''## Beginner Level

### 1. Count Vowels in a List of Strings

👉 Given a list of words, count total vowels in all words.

**Example:**

```python
Input: ["apple", "banana", "cherry"]
Output: 6
```'''

words = ["apple","banana","cherry"]

vowels = "aeiou"

count = 0 

for word in words:
    for ch in word:
        if ch.lower() in vowels:
            count += 1
print("total vowels:", count)