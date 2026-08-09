'''## 🔴 15. Toggle case manually

```python
"HeLLo" → "hEllO"
```

✔ Methods:

- `.isupper()`
- `.islower()`
- `.lower()` / `.upper()`'''

text = "HeLLo"

result = ""

for ch in text:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch
print(result)
