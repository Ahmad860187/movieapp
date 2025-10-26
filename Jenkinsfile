pipeline {
  agent any
  triggers {
    pollSCM('H/2 * * * *')
  }
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/Ahmad860187/movieapp.git'
      }
    }
    stage('Build in Minikube Docker') {
      steps {
        bat '''
        call minikube docker-env --shell=cmd > docker_env.bat
        call docker_env.bat
        docker build -t videostore:latest .
        '''
      }
    }
    stage('Deploy to Minikube') {
      steps {
        bat '''
        kubectl apply -f deployment.yaml
        kubectl rollout status deployment/videostore-deployment
        '''
      }
    }
  }
}
