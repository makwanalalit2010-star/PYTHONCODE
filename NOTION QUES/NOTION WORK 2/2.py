'''### 2. Reverse Each Word in a List

👉 Reverse every string inside a list.

```python
Input: ["hello", "world"]
Output: ["olleh", "dlrow"]
```'''
words = ["hello","world"]

result = []

for word in words:
    result.append(word[::-1])

    print(result)