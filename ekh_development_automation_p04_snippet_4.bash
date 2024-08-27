# Logstash configuration to automate log collection and parsing
     input {
       file {
         path => "/var/log/*.log"
         type => "syslog"
       }
     }

     output {
       elasticsearch {
         hosts => ["localhost:9200"]
       }
       stdout { codec => rubydebug }
     }