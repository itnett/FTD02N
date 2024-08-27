python
import subprocess

def create_user(username):
    try:
        subprocess.run(['sudo', 'adduser', username], check=True)
        print(f"User {username} created successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to create user {username}.")

def delete_user(username):
    try:
        subprocess.run(['sudo', 'deluser', '--remove-home', username], check=True)
        print(f"User {username} deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to delete user {username}.")

def main():
    while True:
        action = input("Enter 'create' to create a user or 'delete' to delete a user: ").strip().lower()
        username = input("Enter username: ").strip()
        
        if action == 'create':
            create_user(username)
        elif action == 'delete':
            delete_user(username)
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()