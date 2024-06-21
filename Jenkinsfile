pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/ajaymisal1908/Test-Automation-Scripts.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Command to install dependencies, if any
                // For example, if you have a requirements.txt for Python
                bat 'C:\\Users\\Ajay Ambadas Misal\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'C:\\Users\\Ajay Ambadas Misal\\AppData\\Local\\Programs\\Python\\Python312\\python.exe Account_Creation.py'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
