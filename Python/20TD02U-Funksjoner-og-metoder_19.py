python
     def find_max(numbers):
         max_number = numbers[0]
         for number in numbers:
             if number > max_number:
                 max_number = number
         return max_number

     print(find_max([1, 3, 2, 5, 4]))  # Output: 5