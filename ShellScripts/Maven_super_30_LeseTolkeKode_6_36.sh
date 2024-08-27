bash
#!/bin/bash

# Opprett bruker
create_user() {
    local username=$1
    sudo adduser $username
}

# Slett bruker
delete_user() {
    local username=$1
    sudo deluser --remove-home $username
}

# Oppdater system
update_system() {
    sudo apt-get update
    sudo apt-get upgrade -y
}

# Hovedskript
main() {
    echo "Enter 'create', 'delete' for user or 'update' to update system:"
    read action
    
    if [ "$action" == "create" ] || [ "$action" == "delete" ]; then
        echo "Enter username:"
        read username
        
        if [ "$action" == "create" ]; then
            create_user "$username"
        elif [ "$action" == "delete" ]; then
            delete_user "$username"
        fi
    elif [ "$action" == "update" ]; then
        update_system
    else
        echo "Invalid action."
    fi
}

main