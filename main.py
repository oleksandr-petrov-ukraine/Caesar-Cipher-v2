def caesar_cipher(text, shift, encrypt=True):
    if not isinstance(text, str):
        raise TypeError('Text must be a string.')

    if not text:
        raise ValueError('Text cannot be empty.')

    if not isinstance(shift, int) or isinstance(shift, bool):
        raise TypeError('Shift must be an integer.')

    if shift < 1:
        raise ValueError('Shift must be a positive integer.')

    shift %= 26  # Normalize shift to be within the range of 0-25

    if not isinstance(encrypt, bool):
        raise TypeError('Encrypt must be a boolean.')

    if not encrypt:
        shift = -shift  # Reverse the shift for decryption
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

    return text.translate(translation_table)

if __name__ == '__main__':
    text = input("Enter the text: ")

    try:
        shift = int(input('Enter the shift value (positive integer): '))
        mode = input('Choose mode (1 - encrypt, 2 - decrypt): ')

        if mode not in ('1', '2'):
            raise ValueError('Invalid mode selected. Choose 1 for encrypt or 2 for decrypt.')

        encrypt = mode == '1'
        
        result = caesar_cipher(text, shift, encrypt)
        print(f'Result: {result}')

    except ValueError as error:
        print(f'Error: {error}')
        
    except TypeError as error:
        print(f'Error: {error}')
