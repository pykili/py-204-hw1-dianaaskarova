user_input = input()
alphabet = ''
for ch in user_input.lower():
    if not ch in alphabet.lower():
        alphabet += ch.lower()
print(alphabet)
