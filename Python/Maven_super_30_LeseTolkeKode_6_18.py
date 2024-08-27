python
import subprocess

def create_user(username):
    """
    Oppretter en ny bruker på en Linux-server.
    """
    try:
        subprocess.run(['sudo', 'adduser', username], check=True)
        print(f"User {username} created successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to create user {username}.")

def delete_user(username):
    """
    Sletter en bruker fra en Linux-server.
    """
    try:
        subprocess.run(['sudo', 'deluser', '--remove-home', username], check=True)
        print(f"User {username} deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to delete user {username}.")

def update_system():
    """
    Utfører en sikkerhetsoppdatering av systemet.
    """


    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'], check=True)
        print("System updated successfully.")
    except subprocess.CalledProcessError:
        print("Failed to update the system.")

def main():
    while True:
        action = input("Enter 'create', 'delete' for user or 'update' to update system: ").strip().lower()
        if action in ['create', 'delete']:
            username = input("Enter username: ").strip()
            if action == 'create':
                create_user(username)
            elif action == 'delete':
                delete_user(username)
        elif action == 'update':
            update_system()
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()