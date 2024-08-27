bash
     # Schedule an automatic vulnerability scan with OpenVAS
     gvm-cli --gmp-username admin --gmp-password admin --xml "<create_task><name>Daily Vulnerability Scan</name><scanner id='xxxx'></scanner></create_task>"