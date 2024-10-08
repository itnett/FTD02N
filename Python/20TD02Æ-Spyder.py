python
def run_windows_server_and_virtualization_examples():
    logger.info("Starter eksempler på Windows Server og virtualisering...")

    install_windows_feature('AD-Domain-Services')
    install_windows_feature('DNS')

    configure_active_directory('example.com', 'P@ssw0rd')

    policy_settings = {
        'HKLM\\Software\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU': 'NoAutoUpdate'
    }
    configure_group_policy('DisableAutoUpdate', policy_settings)

    install_hypervisor('192.168.1.100', 'root', 'root_password')

    logger.info("Eksempler på Windows Server og virtualisering fullført.")

if __name__ == "__main__":
    run_windows_server_and_virtualization_examples()