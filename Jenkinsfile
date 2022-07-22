pipeline{
    agent none
    stages{
        stage("Alpine"){
            agent{
                label 'alpine'
            }
            steps{
                sh 'pip install .'
            }
        }
    }
}