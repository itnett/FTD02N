python
from string_utils import StringUtils

test_string = "hello"
print("Original:", test_string)
print("Reversed:", StringUtils.reverse_string(test_string))
print("Is Palindrome:", StringUtils.is_palindrome(test_string))
print("Uppercase:", StringUtils.to_uppercase(test_string))
print("Vowel Count:", StringUtils.count_vowels(test_string))