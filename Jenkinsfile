pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'contact-list-tests'
        CONTAINER_NAME = 'contact-list-tests'
        ALLURE_REPORTS_DIR = 'allure-results'
        REPORT_PORT = '8090'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // clone repository with the Dockerfile and tests
                git branch: 'main', url: 'https://github.com/isFrost/contact_list_auto_tests.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // build the Docker image
                    sh """
                        docker build -t ${DOCKER_IMAGE} .
                    """
                }
            }
        }

        stage('Run Tests and Generate Allure Results') {
            steps {
                script {
                    // run the container and execute the tests
                    sh """
                        docker run --name ${CONTAINER_NAME} ${DOCKER_IMAGE} sh -c "python3 -m pytest --alluredir=/app/${ALLURE_REPORTS_DIR}"
                    """
                }
            }
        }

        stage('Copy Allure Results to Jenkins') {
            steps {
                script {
                    // copy the allure results from the container to the Jenkins workspace
                    sh """
                        docker cp ${CONTAINER_NAME}:/app/${ALLURE_REPORTS_DIR} ${ALLURE_REPORTS_DIR}
                    """
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                // publish allure report using the Jenkins allure plugin
                allure includeProperties: false, jdk: '', results: [[path: "${ALLURE_REPORTS_DIR}"]]
            }
        }
    }

    post {
        always {
            script {
                // Stop and remove the container to clean up
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                """
            }
        }
    }
}