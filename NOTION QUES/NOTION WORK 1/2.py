'''## 🟡 2. Capitalize each word (without `.title()`)

```python
"hello world" → "Hello World"
```

✔ Methods: `.split()`, `.capitalize()`, `.join()`'''

text = "hello world"

words = text.split()

result = " ".join(word.capitalize() for word in words)
print(result)