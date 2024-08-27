pipeline {
       agent any

       environment {
           ENV = "${env.BRANCH_NAME}"
       }

       stages {
           stage('Build') {
               steps {
                   sh 'make build'
               }
           }
           stage('Test') {
               steps {
                   sh 'make test'
               }
           }
           stage('Deploy') {
               when {
                   branch 'master'
               }
               steps {
                   sh 'make deploy-prod'
               }
           }
           stage('Deploy to Dev') {
               when {
                   branch 'develop'
               }
               steps {
                   sh 'make deploy-dev'
               }
           }
       }
   }