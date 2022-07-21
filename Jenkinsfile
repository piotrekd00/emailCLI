node {   
    stage('Checkout') {
        checkout scm
    }
    stage('Build'){
        sh 'pip install -e .'
        sh 'email-engine'
    }
}