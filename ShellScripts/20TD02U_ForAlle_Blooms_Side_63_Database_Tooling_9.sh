bash
# Installer PMM Client på en MySQL-server
sudo apt-get install pmm-client
pmm-admin config --server pmm-server-url
pmm-admin add mysql --user root --password ditt_passord

# Analyser ytelsesdataene i PMM-webgrensesnittet