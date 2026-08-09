'''## 🟡 3. Remove punctuation from string

```python
"hello!!! world??" → "hello world"
```

✔ Methods: `.replace()` (multiple times), `.isalpha()`, `.join()`'''

text = "hello!!! world??"

result = "".join(ch for ch in text if ch.isalpha() or ch == " ")
print(result)