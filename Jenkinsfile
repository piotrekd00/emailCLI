node {
    stage('Checkout') {
        print(env.BRANCH_NAME)
        if (env.BRANCH_NAME == 'main') {
            continue
        } else {
            throw new Exception('wrong branch')
        }
    }
    stage('Build'){
        sh 'pip install -e .'
    }
}