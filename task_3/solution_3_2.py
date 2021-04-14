n = 10
alphabet = ''
for i in range(n):
    # вводим строку (одну из 10)
    user_input = input()
    for ch in user_input.lower():
        if not ch in alphabet.lower():
            alphabet += ch.lower()
print(alphabet)
