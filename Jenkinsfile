pipeline {
    agent {
        docker {
            image 'amd-pytest:latest'
        }
    }
    stages {
        // stage('Build') {
        //     steps {
        //         //sh 'pip install webdriver-manager'
        //         //sh 'pip install selenium'
        //         //sh 'mkdir /app/screenshots'
        //     }
        // }
        stage('Test') {
            steps {
                sh 'python chrome.py'
            }
        }
    }
}
