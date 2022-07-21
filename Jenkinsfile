node {   
    stage('Checkout') {
        print(env.BRANCH_NAME)
        checkout
    }
    stage('Build'){
        sh 'pip install -e .'
    }
}