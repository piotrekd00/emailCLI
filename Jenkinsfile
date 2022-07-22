pipeline{
    agent none
    stages{
        stage("Arch"){
            agent{
                label 'arch'
            }
            steps{
                sh 'pip install .'
                sh 'email-engine -p emails'
            }
        }
    }
}