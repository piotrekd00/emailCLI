node {   
    stage('Checkout') {
        checkout scm
    }
    stage('Build'){
        sh 'pip install -e .'
        print('Ensure it is working')
        sh 'email-engine'
    }
    stage('Test duplicates'){
        sh 'email-engine -rd'
    }
    stage('Test incorrect emails'){
        sh 'email-engine -rd -ic'
    }
    stage('Test search'){
        sh 'email-engine -rd -s agustin'
    }
    stage('Test domains'){
        sh 'email-engine -gbd'
    }
    stage('Test logs'){
        sh 'email-engine -feil email-sent.logs'
    }
}