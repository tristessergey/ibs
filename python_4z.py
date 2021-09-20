slovar = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
new_s = {}
a = 0
for key in slovar:
    if slovar[key] >= 3: 
        a = a + 1
        new_s[a] = slovar[key]
print(new_s)
