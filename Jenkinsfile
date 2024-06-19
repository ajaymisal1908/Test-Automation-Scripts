pipeline {
    agent any

    environment {
        CHROME_DRIVER = "C:/Users/Ajay Ambadas Misal/.wdm/drivers/chromedriver/win64/126.0.6478.62/chromedriver-win32/chromedriver.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ajaymisal1908/Test-Automation-Scripts.git'
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest Account_Creation.py'
            }
        }
    }

    post {
        always {
            junit '**/test-reports/*.xml'
            archiveArtifacts artifacts: '**/screenshots/*.png', allowEmptyArchive: true
        }
        success {
            slackSend channel: '#test-results', message: 'All tests passed!'
        }
        failure {
            slackSend channel: '#test-results', message: 'Some tests failed. Check the Jenkins job for details.'
        }
    }
}
