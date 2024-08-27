python
   def countdown(num):
       while num > 0:
           yield num
           num -= 1

   for number in countdown(5):
       print(number)