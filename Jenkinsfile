pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-mock-app"
        CONTAINER_NAME = "flask-mock-container"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker image...'
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Deploy (Local Run)') {
            steps {
                echo 'Deploying the container...'
                sh '''
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
                '''
                sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest"
            }
        }
    }
}