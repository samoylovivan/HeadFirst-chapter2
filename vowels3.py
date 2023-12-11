
vowels = []
for ch in 'aeiou':
    vowels.append(ch)
word = input('Provide a word to search for vowels: ')
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
