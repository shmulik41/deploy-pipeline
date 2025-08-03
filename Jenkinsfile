pipeline {
    agent any

    parameters {
        choice(name: 'SERVICE_NAME', choices: ['service1', 'service2'], description: 'Select the service to deploy')
    }

    environment {
        DOCKERHUB_USER = 'shmulik41'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('📦 Show Selected Service') {
            steps {
                echo "Selected service: ${params.SERVICE_NAME}"
            }
        }

        stage('🐳 Build Docker Image') {
            steps {
                script {
                    def imageName = "${DOCKERHUB_USER}/${params.SERVICE_NAME}:${IMAGE_TAG}"
                    sh "docker build -t ${imageName} ./services/${params.SERVICE_NAME}"
                }
            }
        }

        stage('🔐 Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh "echo \$PASSWORD | docker login -u \$USERNAME --password-stdin"
                }
            }
        }

        stage('🚀 Push to DockerHub') {
            steps {
                script {
                    def imageName = "${DOCKERHUB_USER}/${params.SERVICE_NAME}:${IMAGE_TAG}"
                    sh "docker push ${imageName}"
                }
            }
        }

        stage('🛠 Deploy with Ansible') {
            steps {
                sh 'ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ansible/inventory.ini ansible/deploy-playbook.yml -e "service_name=${params.SERVICE_NAME}"'
            }
        }
    }
}




