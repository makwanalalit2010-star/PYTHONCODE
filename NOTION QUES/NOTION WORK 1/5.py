'''## 🟡 5. Extract only alphabets

```python
"a1b2c3!" → "abc"
```

✔ Methods: `.isalpha()`, `.join()`'''

s = "a1b2c3"

str = "". join(ch for ch in s if ch.isalpha())

print(str)