'''## 🔴 10. Convert sentence to snake_case

```python
"Hello World Python" → "hello_world_python"
```

✔ Methods: `.lower()`, `.split()`, `.join()`'''

text = "Hello World Python"

snake_case = "_".join(text.lower().split())

print(snake_case)
