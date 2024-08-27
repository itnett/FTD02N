pipeline {
       agent any

       stages {
           stage('Checkout') {
               steps {
                   checkout scm
               }
           }

           stage('Install Dependencies') {
               steps {
                   sh 'sudo apt-get update'
                   sh 'sudo apt-get install -y nmap gobuster nikto python3 python3-pip'
                   sh 'pip3 install cherrypy'
               }
           }

           stage('Run Scan') {
               steps {
                   sh 'python3 automate_scan.py'
               }
           }
       }
   }