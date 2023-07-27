# Week 3: Assignment (Python_1)

sentence = input("Enter a sentence")
sentence = sentence.lower()
#print(sentence)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet2 = alphabet * 2
cipher = []

letter = 0

while letter < 26:
    #print(replacement)
    replacement = alphabet2[letter + 5]
    cipher.append(replacement)
    letter += 1

new_sent = []

for char in sentence:
    if char in alphabet2:
        indexof = alphabet2.index(char)
        var = cipher[indexof]
        new_sent.append(var)
    else:
        new_sent.append(char)

translated_sent = "".join(new_sent)
print("The encrypted sentence is:", translated_sent)