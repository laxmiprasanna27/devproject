pipeline {
    agent any
    stages {
        stage("Build Docker image") {
            steps {
                echo "Build Docker image"
                bat "docker build -t  weight-cal:v1 ."
            }
        }
        stage("Docker Login") {
            steps {
                bat "docker login -u laxmiprasanna11 -p laxmiprasanna@11"
            }
        }
        stage("push Docker image to docker hub") {
            steps {
                echo "push Docker image to docker hub"
                bat "docker tag   weight-cal:v1 laxmiprasanna11/case_studys:t4"
                bat "docker push laxmiprasanna11/case_studys:t4"
            }
        }
        stage("Deploy to kubernetes") {
            steps {
                echo "Deploy to kubernetes"
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }
    }
    post {
        success {
            echo "Pipeline executed successfully"
        }
        failure {
            echo "pipeline failed. Please check the logs"
        }
    }
}
