pipeline {
    agent {
        docker {
            image 'python'
        }
    }
    stages {
        stage('Build') {
            steps {
              sh 'pip install selenium'
            }
        }
        stage('Test') {
            steps {
              sh 'python python_org_search.py'
            }
        }
    }
}
