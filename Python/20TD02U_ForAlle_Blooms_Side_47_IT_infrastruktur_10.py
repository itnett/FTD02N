python
      def check_access(user):
          allowed_users = ['admin', 'user1', 'user2']
          if user in allowed_users:
              return True
          else:
              return False

      user = 'admin'
      if check_access(user):
          print("Access granted")
      else:
          print("Access denied")