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
        //         sh 'pip install selenium'
        //     }
        // }
        stage('Test') {
            steps {
                sh 'python firefox.py'
            }
        }
    }
}
