python
   class A:
       def method_a(self):
           return "Method A"

   class B:
       def method_b(self):
           return "Method B"

   class C(A, B):
       pass

   c = C()
   print(c.method_a())
   print(c.method_b())