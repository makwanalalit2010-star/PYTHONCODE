'''## 🔴 11. Remove first and last character of each word

```python
"hello world" → "ell orl"
```

✔ Methods: `.split()`, slicing, `.join()`'''

rtrt = "hello world"

words = rtrt.split()
result = []

for word in words:
    result.append(word[1:-1])

    output = " ".join(result)

print(output)