node {
    stage('Checkout') {
        if (env.BRANCH_NAME == 'master') {
            continue
        } else {
            throw new Exception('wrong branch')
        }
    }
    stage('Build'){
        sh 'pip install -e .'
    }
}