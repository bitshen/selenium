pipeline {
    agent {
        docker {
            image 'selenium-python:latest'
        }
    }
    stages {
        // stage('Build') {
        //     steps {
        //         sh 'pip install webdriver-manager'
        //         sh 'pip install selenium'
        //     }
        // }
        stage('Test') {
            steps {
                sh 'python python_org_search.py'
            }
        }
    }
}
