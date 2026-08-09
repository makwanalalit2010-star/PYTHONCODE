'''## 🔴 7. Remove duplicate words

```python
"this is is a test test" → "this is a test"
```

✔ Methods: `.split()`, `.join()`, membership check'''

'''text = "this is is a test test"

words = text.split()
result = []

for word in words:
    if word not in result:
        result.append(word)

output = " ".join(result)

print(output)'''


s = "this is is a test test"

words = s.split()
m = []

for word in words:
    if word not in m:
        m.append(word)

er = " ".join(m)
print(er)
