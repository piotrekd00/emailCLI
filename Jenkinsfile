pipeline{
    agent none
    stages{
        stage("Arch"){
            agent{
                label 'arch'
            }
            steps{
                sh 'pacman -S --noconfirm python3'
                sh 'PATH="$PATH:/home/jenkins/.local/bin"'
                sh 'pip install .'
                sh 'email-engine -p emails'
            }
        }
    }
}