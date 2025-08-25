pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'smartfarm-app'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        DOCKER_HUB_REPO = 'your-dockerhub-username/smartfarm-app'
        DOCKER_HUB_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        stage('Test Flask App') {
            steps {
                sh '''
                    docker run -d --name test_flask -p 5000:5000 ${DOCKER_IMAGE}:${DOCKER_TAG}
                    sleep 10
                    curl -f http://localhost:5000/ || exit 1
                    docker stop test_flask && docker rm test_flask
                '''
            }
        }

        stage('Push to Docker Hub') {
            when { branch 'main' }
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh '''
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                        docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_HUB_REPO}:${DOCKER_HUB_TAG}
                        docker push ${DOCKER_HUB_REPO}:${DOCKER_HUB_TAG}
                        docker logout
                    '''
                }
            }
        }
    }

    post {
        always {
            sh "docker system prune -f || true"
        }
    }
}
