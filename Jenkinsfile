pipeline {
    agent {
        docker {
            image 'python:3.10.7-alpine'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
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

