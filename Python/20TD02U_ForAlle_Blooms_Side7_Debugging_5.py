python
   def test_innlogging_system():
       bruker = opprett_bruker("testbruker", "passord123")
       innlogget = logg_inn("testbruker", "passord123")
       assert innlogget == True