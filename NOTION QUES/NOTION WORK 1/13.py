'''
## 🔴 13. Count words ignoring punctuation

```python
"Hello, world! Python is great." → 5
```

✔ Methods:

- `.replace()` OR `.isalpha()`
- `.split()`'''


sentence = "Hello, world! Python is great."

sentence = sentence.replace(",","")
sentence = sentence.replace("!","")
sentence = sentence.replace(".","")


words = sentence.split()

print("word count:",len(words))