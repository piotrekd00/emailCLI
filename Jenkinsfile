node {
    stage('Checkout') {
        print(env.BRANCH_NAME)
    }
    stage('Build'){
        sh 'pip install -e .'
    }
}