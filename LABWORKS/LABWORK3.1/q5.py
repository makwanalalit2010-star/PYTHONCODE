'''Find the position of the word "Al" in the sentence "Machine Learning and Al are

trending"

Replace "Al" with "Artificial Intelligence" in the above sentence.

Count how many times the word "data" appears in "data data mining and big data'''

str1 = "machin learning and AI are trending"

position = str1.find("AI")
print("position of 'AI':",position)

new_str = str1.replace("AI","artificial intelligence")
print("after replacing:",new_str)

text = "data  data minning data data big data"
count = text.count("data")
print(count)