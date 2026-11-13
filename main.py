shift = 5
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
translation_table = str.maketrans(alphabet, shifted_alphabet)
text = 'Hello, World!'
encrypted_text = text.translate(translation_table)
print(encrypted_text)