python
     # test_oop_example.py
     from oop_example import Dog, Cat

     def test_dog_speak():
         dog = Dog("Rex")
         assert dog.speak() == "Rex says Woof!"

     def test_cat_speak():
         cat = Cat("Whiskers")
         assert cat.speak() == "Whiskers says Meow!"