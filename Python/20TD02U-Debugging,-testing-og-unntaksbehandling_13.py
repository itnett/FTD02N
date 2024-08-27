python
   import pytest

   @pytest.mark.parametrize("a, b, expected", [
       (1, 1, 2),
       (2, 3, 5),
       (3, 5, 8),
   ])
   def test_add(a, b, expected):
       from kalkulator import Calculator
       calc = Calculator()
       assert calc.add(a, b) == expected