pipeline {
    agent {
        docker {
            image 'webtest-python:latest'
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
                python chrome.py
            }
        }
    }
}
