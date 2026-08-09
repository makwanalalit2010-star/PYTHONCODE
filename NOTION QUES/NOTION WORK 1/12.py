'''## 🔴 12. Find longest word

```python
"I love Python programming" → "programming"
```

✔ Methods: `.split()`, `max()`'''

twxt = "I love python programming"

words = twxt.split()

longest = max(words,key=len)

print(longest)