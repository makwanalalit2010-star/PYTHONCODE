'''## 🔴 6. Reverse words in a sentence

```python
"I love Python" → "Python love I"
```

✔ Methods: `.split()`, slicing, `.join()`'''

text = "i love python"

result = " ".join(text.split()[::-1])
print(result)