python
   def caesar_cipher(text, shift):
       """Encrypt text using Caesar cipher with a given shift."""
       encrypted_text = ""
       for char in text:
           if char.isalpha():
               base = ord('a') if char.islower() else ord('A')
               encrypted_char = chr((ord(char) - base + shift) % 26 + base)
               encrypted_text += encrypted_char
           else:
               encrypted_text += char
       return encrypted_text

   try:
       plaintext = input("Enter the text to encrypt: ")
       shift = int(input("Enter the shift value: "))
       encrypted = caesar_cipher(plaintext, shift)
       print("Encrypted text:", encrypted)
   except ValueError:
       print("Invalid shift value. Please enter an integer.")