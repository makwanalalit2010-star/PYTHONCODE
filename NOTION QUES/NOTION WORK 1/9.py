'''## 🔴 9. Mask a phone number

```python
"9876543210" → "987*****10"
```

✔ Methods: slicing + string multiplication'''

phone = "9876543210"

masked = phone[:3] + "*" * 5 + phone[-2:]

print(masked)

