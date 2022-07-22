pipeline{
    agent none
    stages{
        stage("Build"){
            parallel{
                stage("Alpine"){
                    agent{
                        label 'alpine'
                    }
                    steps{
                        sh 'pip install .'
                        sh 'email-engine -p emails'
                    }
                }
                        stage("Arch"){
                    agent{
                        label 'arch'
                    }
                    steps{
                        sh 'pip install .'
                        sh 'email-engine -p emails'
                    }
                }
                        stage("Debian"){
                    agent{
                        label 'debian'
                    }
                    steps{
                        sh 'pip install .'
                        sh 'email-engine -p emails'
                    }
                }
            }   
        }
    }   
}