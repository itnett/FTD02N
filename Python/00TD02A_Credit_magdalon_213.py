python
   user_access = {
       "admin": ["read", "write", "execute"],
       "user1": ["read"],
       "user2": ["read", "write"],
   }

   def check_access(username, action):
       """Check if a user has permission to perform an action."""
       return action in user_access.get(username, [])

   username = input("Enter username: ")
   action = input("Enter action: ")
   if check_access(username, action):
       print("Action permitted.")
   else:
       print("Action not permitted.")