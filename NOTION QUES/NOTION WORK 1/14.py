'''## 🔴 14. Check if sentence is palindrome (ignore spaces)

```python
"nurses run" → True
```

✔ Methods:

- `.replace()`
- slicing'''


text = "nurses run"

text = text.replace(" ", "")

if text == text[::-1]:
    print(True)
else:
    print(False)