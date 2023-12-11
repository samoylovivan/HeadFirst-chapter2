
vowels = []
for ch in 'aeiou':
    vowels.append(ch)
word = 'Milliways'
for letter in word:
    if letter in vowels:
        print(letter)
