pipeline{
    agent none
    stages{
        stage("Build"){
            parallel{
                stage("Alpine"){
                    agent{
                        label 'alpine'
                    }
                    stages{
                        stage('Build'){
                            steps{
                                sh '''
                                pip install .
                                '''
                            }
                        }
                        stage('Test'){
                            steps{
                                sh '''
                                cd tests
                                python3 -m unittest tests.py
                                '''
                            }
                        }
                    }
                }
                        stage("Arch"){
                    agent{
                        label 'arch'
                    }
                    stages{
                        stage('Build'){
                            steps{
                                sh '''
                                pip install .
                                '''
                            }
                        }
                        stage('Test'){
                            steps{
                                sh '''
                                cd tests
                                python3 -m unittest tests.py
                                '''
                            }
                        }
                    }
                }
                        stage("Debian"){
                    agent{
                        label 'debian'
                    }
                    stages{
                        stage('Build'){
                            steps{
                                sh '''
                                pip install .
                                '''
                            }
                        }
                        stage('Test'){
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
    }   
}