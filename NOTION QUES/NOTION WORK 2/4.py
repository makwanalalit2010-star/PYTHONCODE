'''### 4. Remove Duplicate Characters from Each String 👉 Remove repeating characters from each word.
python
Input: ["hello", "banana"]
Output: ["helo", "ban"]'''

words = ["hello","banana"]

result = []

for word in words:
    new_word = ""


    for ch in word:
        if ch not in new_word:
            new_word += ch
    result.append(new_word)
print(result)