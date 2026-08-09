'''## 🟡 4. Extract only digits from string

```python
"a1b2c3" → "123"
```

✔ Methods: `.isdigit()`, `.join()`'''

a = "a1b2c3"

result = ""

for ch in a:
    if ch.isdigit():
        result += ch
print(result)
