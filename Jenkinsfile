pipeline {
    agent any

    parameters {
        choice(
            name: 'SERVICE_NAME',
            choices: ['service1', 'service2'],
            description: 'בחר את השירות שברצונך לבנות ולפרוס'
        )
    }

    environment {
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo "🚧 בונה Docker Image עבור השירות: ${params.SERVICE_NAME}"
                sh """
                docker build -t shmulik41/${params.SERVICE_NAME}:${IMAGE_TAG} ./services/${params.SERVICE_NAME}
                """
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo "📤 דוחף את התמונה ל־DockerHub"
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh '''
                    echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USER" --password-stdin
                    docker push shmulik41/${SERVICE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo "🚀 מריץ Ansible לפריסת השירות"
                sh """
                ansible-playbook -i ansible/inventory.ini ansible/deploy-playbook.yml --extra-vars "service_name=${params.SERVICE_NAME}"
                """
            }
        }
    }
}

