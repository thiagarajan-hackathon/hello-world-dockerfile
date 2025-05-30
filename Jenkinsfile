pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/thiagarajan-hackathon/hello-world-dockerfile.git' // Replace with your repository URL
        IMAGE_NAME = 'Hackathon-image' // Replace with your desired Docker image name
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                git branch: 'master', url: "${REPO_URL}" // Replace 'main' with your branch name if different
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker image...'
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
