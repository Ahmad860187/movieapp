pipeline {
  agent any
  options { skipDefaultCheckout() }

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/Ahmad860187/movieapp.git',
            branch: 'master',
            changelog: false,
            poll: false
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        bat '''
        minikube docker-env > tmp_env.bat
        call tmp_env.bat
        docker build -t mydjangoapp:latest .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
        kubectl apply -f deployment.yaml
        kubectl apply -f service.yaml
        kubectl rollout status deployment/mydjangoapp
        '''
      }
    }
  }
}
