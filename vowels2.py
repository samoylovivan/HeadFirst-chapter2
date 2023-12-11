
vowels = []
for ch in 'aeiou':
    vowels.append(ch)
word = 'Milliways'
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
