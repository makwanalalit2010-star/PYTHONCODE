'''### 3. Find Longest Word 👉 From a list of strings, find the longest word.
python
Input: ["cat", "elephant", "dog"]
Output: "elephant"'''

words = ["cat","elephant","dog"]

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)