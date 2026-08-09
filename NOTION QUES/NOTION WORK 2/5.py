'''### 5. Filter Words Starting with a Vowel

👉 Return only words that start with vowels.

```python
Input: ["apple", "dog", "elephant"]
Output: ["apple", "elephant"]
```'''

words = ["apple","dog","elephant"]

result = []

for word in words:
    if word[0].lower() in "aeiou":
        result.append(word)
print(result)