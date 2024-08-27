define service {
        use                 generic-service
        host_name           localhost
        service_description HTTP
        check_command       check_http
        notifications_enabled 1
    }