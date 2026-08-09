'''### 13. Flatten List of Sentences into Words

👉 Convert list of sentences into list of words.

```python
Input: ["Python is fun", "I love coding"]
Output: ["Python", "is", "fun", "I", "love", "coding"]
```'''

a = ["python is fun", "i love coding"]
b=a[0].split()
c=a[1].split()
print(b+c)