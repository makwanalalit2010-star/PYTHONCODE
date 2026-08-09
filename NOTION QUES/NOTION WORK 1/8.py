'''## 🔴 8. Check if email is valid (basic)

```python
"test@gmail.com" → True
```

✔ Conditions:

- contains `"@"`
- endswith `.com`

✔ Methods: `.count()`, `.endswith()`, `.find()`'''


email = "test@gmail.com"

if email.count("@") == 1 and email.endswith(".com") and email.find("@") > 0:
    print(True)
else:
    print(False)