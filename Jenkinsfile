pipeline {
    agent any

    environment {
        CHROME_DRIVER = "C:/Users/Ajay Ambadas Misal/.wdm/drivers/chromedriver/win64/126.0.6478.62/chromedriver-win32/chromedriver.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                git clone 'https://github.com/ajaymisal1908/Test-Automation-Scripts.git'
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
}
