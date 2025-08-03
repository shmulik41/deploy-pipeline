pipeline {
    agent any

    parameters {
        choice(name: 'service_name', choices: ['service1', 'service2'], description: 'Select the service to deploy')
    }

    environment {
        IMAGE_NAME = "shmulik41/${params.service_name}:latest"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo "🚧 בונה Docker Image עבור השירות: ${params.service_name}"
                sh "docker build -t ${IMAGE_NAME} ./services/${params.service_name}"
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "📤 דוחף את Docker Image ל־DockerHub"
                sh "docker push ${IMAGE_NAME}"
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo "🚀 מפיץ עם Ansible"
                sh '''
                #!/bin/bash
                ansible-playbook -i ansible/inventory.ini ansible/deploy-playbook.yml \
                    -e service_name=_



