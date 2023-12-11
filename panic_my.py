phrase = 'Don`t panic!'
plist = list(phrase)
print(phrase)
print(plist)

tmp = []
for ch in 'on tap':
    if ch in plist:
        tmp.append(ch)

plist = tmp.copy()

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
