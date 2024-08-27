python
class StringUtils:
    @staticmethod
    def reverse_string(s):
        return s[::-1]

    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

    @staticmethod
    def to_uppercase(s):
        return s.upper()

    @staticmethod
    def count_vowels(s):
        return sum(1 for char in s.lower() if char in 'aeiou')

# Example usage
if __name__ == "__main__":
    test_string = "racecar"
    print("Original:", test_string)
    print("Reversed:", StringUtils.reverse_string(test_string))
    print("Is Palindrome:", StringUtils.is_palindrome(test_string))
    print("Uppercase:", StringUtils.to_uppercase(test_string))
    print("Vowel Count:", StringUtils.count_vowels(test_string))