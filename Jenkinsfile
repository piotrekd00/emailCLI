node {   
    stage('Checkout') {
        print(env.BRANCH_NAME)
        checkout scm
    }
    stage('Build'){
        sh 'pip install -e .'
    }
}