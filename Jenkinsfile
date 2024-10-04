pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'contact-list-tests' // Replace with your Docker image name
        CONTAINER_NAME = 'contact-list-tests'  // Replace with your desired container name
        ALURE_REPORTS_DIR = 'allure-results'
        REPORT_PORT = '8080'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Assuming your Dockerfile is part of a Git repository
                git branch: 'main', url: 'https://github.com/isFrost/contact_list_auto_tests.git' // Replace with your repo
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image based on the Dockerfile
                    sh """
                        docker build -t ${DOCKER_IMAGE} .
                    """
                }
            }
        }

        stage('Run Tests and Generate Allure Report') {
            steps {
                script {
                    // Run the container with the built image
                    sh """
                        docker run --name ${CONTAINER_NAME} -d -p ${REPORT_PORT}:${REPORT_PORT} ${DOCKER_IMAGE}
                    """

                    // Optionally: execute tests or other steps (already in Dockerfile)
                    // Jenkins will listen to the process outputs

                    // Wait for the tests and allure server to start properly (adjust timeout as necessary)
                    sleep 20

                    // Optionally: print the logs to see what happened
                    sh """
                        docker logs ${CONTAINER_NAME}
                    """
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                script {
                    // Copy the allure results from the container to Jenkins workspace
                    sh """
                        docker cp ${CONTAINER_NAME}:/app/${ALURE_REPORTS_DIR} ${ALURE_REPORTS_DIR}
                    """
                }

                // Publish Allure report using the Jenkins Allure plugin
                allure includeProperties: false, jdk: '', results: [[path: "${ALURE_REPORTS_DIR}"]]
            }
        }
    }

    post {
        always {
            script {
                // Stop and remove the container
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                """
            }
        }
    }
}