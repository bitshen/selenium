pipeline {
    agent {
        docker {
            image 'amd-pytest:latest'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python chrome.py'
            }
        }
    }
}
