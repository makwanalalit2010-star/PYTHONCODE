'''Q.18 Create a function that takes a list of words and returns two lists:
1. Words starting with vowels
2. Words starting with consonants'''


def split_words(words):
    vowels = []
    consonants = []

    for word in words:
        if word[0].lower() in 'aeoiu':
            vowels.append(word)
        else:
            consonants.append(word)

            return vowels, consonants
lst = ["Apple", "Ball", "Orange", "Cat", "Elephant", "Dog"]

vowel,consonant = split_words(lst)

print("words starting with vowels: ",vowel)
print("words starting with consonants: ",consonant)