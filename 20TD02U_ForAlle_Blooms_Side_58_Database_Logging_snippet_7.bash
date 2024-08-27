# Eksempel på konfigurering av Logstash for å samle loggdata fra flere kilder
input {
    file {
        path => "/var/log/mysql/error.log"
        type => "mysql-error-log"
    }
    file {
        path => "/var/log/nginx/access.log"
        type => "nginx-access-log"
    }
}

output {
    elasticsearch {
        hosts => ["localhost:9200"]
    }
    stdout { codec => rubydebug }
}