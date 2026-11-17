# Caesar Cipher v2

A Python implementation of the Caesar Cipher using Python's built-in string translation methods.

## Project Overview

This project is an improved version of my original Caesar Cipher implementation.

The first version used a `for` loop to process each character individually. In the second version, I replaced manual character processing with Python's built-in `str.maketrans()` and `str.translate()` methods.

The goal was to create cleaner, more reusable code with input validation and exception handling.

## Features

- Encrypt and decrypt text.
- Support for uppercase and lowercase letters.
- Preserve spaces, numbers, and special characters.
- Validate input types and values.
- Handle invalid input using exceptions.
- Normalize shift values using the modulo operator.
- Use a single function for encryption and decryption.
- Interactive console interface for selecting encryption or decryption mode.

## How It Works

The Caesar Cipher is a substitution cipher that shifts each letter in the alphabet by a specified number of positions.

For example, with a shift of 3:

**Encryption:**
```text
HELLO WORLD → KHOOR ZRUOG
```

**Decryption:**
```text
KHOOR ZRUOG → HELLO WORLD
```

The implementation uses:

- `str.maketrans()` to create a character translation table.
- `str.translate()` to apply the translation.
- The modulo operator (`%`) to normalize the shift value.

## Usage

### Run the Program

Execute the Python script:

```bash
python3 main.py
```

Enter the text, shift value, and select the desired operation.

### Interactive Mode

The program supports two modes:

- `1` — Encrypt text.
- `2` — Decrypt text.

### Encryption Example

```text
Enter the text: Hello, World!
Enter the shift value (positive integer): 3
Choose mode (1 - encrypt, 2 - decrypt): 1
Result: Khoor, Zruog!
```

### Decryption Example

```text
Enter the text: Khoor, Zruog!
Enter the shift value (positive integer): 3
Choose mode (1 - encrypt, 2 - decrypt): 2
Result: Hello, World!
```

### Using the Function

The main function:

```python
def caesar_cipher(text, shift, encrypt=True):
```

Parameters:

| Parameter | Type | Description |
|---|---|---|
| `text` | `str` | Text to encrypt or decrypt. |
| `shift` | `int` | Positive number of positions to shift letters. |
| `encrypt` | `bool` | `True` for encryption, `False` for decryption. |

#### Encryption Example

```python
from main import caesar_cipher

encrypted_text = caesar_cipher("Hello, World!", 3)
print(encrypted_text)
```

Output:

```text
Khoor, Zruog!
```

#### Decryption Example

```python
from main import caesar_cipher

decrypted_text = caesar_cipher("Khoor, Zruog!", 3, encrypt=False)
print(decrypted_text)
```

Output:

```text
Hello, World!
```

## Input Validation

The function validates all arguments before processing the text.

It raises:

- `TypeError` if the text is not a string.
- `ValueError` if the text is empty.
- `TypeError` if the shift is not an integer.
- `ValueError` if the shift is less than 1.
- `TypeError` if the encryption parameter is not a boolean.

## Technologies Used

- Python 3
- Git
- GitHub

No external Python libraries are required.

## Project Evolution

**Version 1**

- Used a `for` loop for character-by-character processing.
- Manually calculated character positions.
- Implemented encryption and decryption using a mode parameter.

**Version 2**

- Replaced manual character processing with `str.maketrans()` and `str.translate()`.
- Introduced a reusable function with an optional encryption parameter.
- Added comprehensive input validation.
- Improved exception handling and code readability.
- Added interactive mode selection for encryption and decryption.

## What I Learned

- Writing reusable Python functions.
- Working with string methods.
- Using `str.maketrans()` and `str.translate()`.
- Handling exceptions with `raise`.
- Validating function arguments.
- Using boolean parameters.
- Working with Git and GitHub.
- Refactoring code to improve readability and maintainability.

---

*This project is part of my ongoing journey of learning Python programming.*