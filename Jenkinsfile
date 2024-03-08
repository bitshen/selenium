pipeline {
    agent {
        docker {
            image 'selenium'
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
