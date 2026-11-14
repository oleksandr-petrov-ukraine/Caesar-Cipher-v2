def caesar_cipher(text, shift):
    if not isinstance(text, str):
        raise TypeError('Text must be a string.')

    if not text:
        raise ValueError('Text cannot be empty.')

    if not isinstance(shift, int) or isinstance(shift, bool):
        raise TypeError('Shift must be an integer.')

    if shift < 1:
        raise ValueError('Shift must be a positive integer.')

    shift = shift % 26  # Normalize shift to be within the range of 0-25
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

    return text.translate(translation_table)

encrypted_text = caesar_cipher("hello world", 3)
print(encrypted_text)
