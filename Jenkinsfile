pipeline{
    agent any
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