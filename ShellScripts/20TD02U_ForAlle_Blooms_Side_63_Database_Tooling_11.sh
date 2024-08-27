bash
# Liquibase script example for CI/CD
liquibase updateSQL > updates.sql
liquibase update

# Integrer Liquibase i Jenkins Pipeline
pipeline {
    agent any
    stages {
        stage('Database Update') {
            steps {
                sh 'liquibase update'
            }
        }
    }
}