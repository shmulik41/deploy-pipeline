pipeline {
    agent any

    parameters {
        choice(name: 'SERVICE_NAME', choices: ['service1', 'service2'], description: 'Select the service to deploy')
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
                    def imageName = "${params.SERVICE_NAME}:test"
                    sh "docker build -t ${imageName} ./services/${params.SERVICE_NAME}"
                }
            }
        }
    }
}

