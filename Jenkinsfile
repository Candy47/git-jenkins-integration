pipeline {
    agent any
    environment {
        GIT_CREDENTIALS = credentials('github-credentials') // ID of your GitHub credentials
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/EyesOnCloud/git-jenkins-integration.git',
                    credentialsId: 'github-credentials'
            }
        }
        stage('Set Up Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || echo "No requirements file"'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover'
                sh 'python3 test_main.py'
            }
        }
    }
}
