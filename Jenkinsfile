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
                        sh '''
                        pip install .
                        '''
                    }
                }
                        stage("Arch"){
                    agent{
                        label 'arch'
                    }
                    steps{
                        sh '''
                        pip install .
                        '''
                    }
                }
                        stage("Debian"){
                    agent{
                        label 'debian'
                    }
                    steps{
                        sh '''
                        pip install .
                        '''
                    }
                }
            }   
        }
        stage("Tests"){
            parallel{
                stage("Alpine"){
                    agent{
                        label 'alpine'
                    }
                    steps{
                        sh '''
                        cd tests
                        python3 -m unittest tests.py
                        '''
                    }
                }
                        stage("Arch"){
                    agent{
                        label 'arch'
                    }
                    steps{
                        sh '''
                        cd tests
                        python3 -m unittest tests.py
                        '''
                    }
                }
                        stage("Debian"){
                    agent{
                        label 'debian'
                    }
                    steps{
                        sh '''
                        cd tests
                        python3 -m unittest tests.py
                        '''
                    }
                }
            }   
        }
    }   
}