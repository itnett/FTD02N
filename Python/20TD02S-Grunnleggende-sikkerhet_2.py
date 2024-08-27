python
class User:
    def __init__(self, username, roles):
        self.username = username
        self.roles = roles

class RBAC:
    def __init__(self):
        self.permissions = {}
    
    def add_permission(self, role, permission):
        if role not in self.permissions:
            self.permissions[role] = set()
        self.permissions[role].add(permission)
    
    def check_permission(self, user, permission):
        for role in user.roles:
            if permission in self.permissions.get(role, []):
                return True
        return False

# Example usage
rbac = RBAC()
rbac.add_permission("admin", "read")
rbac.add_permission("admin", "write")
rbac.add_permission("user", "read")

user1 = User("alice", ["user"])
user2 = User("bob", ["admin"])

print(f"User1 read permission: {rbac.check_permission(user1, 'read')}")
print(f"User1 write permission: {rbac.check_permission(user1, 'write')}")
print(f"User2 read permission: {rbac.check_permission(user2, 'read')}")
print(f"User2 write permission: {rbac.check_permission(user2, 'write')}")