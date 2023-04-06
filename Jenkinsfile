pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'docker info'
                sh 'docker pull python:2-alpine'
                sh 'python --version'
            }
        }
    }
}
