pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/myrepo/openshift-pipeline.git'
            }
        }
        stage('Build and Deploy') {
            steps {
                script {
                    openshift.withCluster() {
                        openshift.withProject("myproject") {
                            def build = openshift.selector("bc", "myapp").startBuild()
                            build.logs('-f')
                        }
                    }
                }
            }
        }
    }
}