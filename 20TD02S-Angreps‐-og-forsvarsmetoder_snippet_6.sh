wget https://releases.hashicorp.com/vault/1.7.0/vault_1.7.0_linux_amd64.zip
    unzip vault_1.7.0_linux_amd64.zip
    sudo mv vault /usr/local/bin/
    vault server -config=config.hcl