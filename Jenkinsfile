pipeline{
    
    agent any
    stages
    {
        stage('Clone Repo'){
            steps{
                script{
                    if(fileExists('/home/jenkins/.jenkins/workspace/docker-project2/')){
                        dir('docker-project2'){ sh 'git pull https://github.com/M-Talha-Saeed/docker-project2.git main'}
                    }
                    else{
                        sh 'git clone https://github.com/M-Talha-Saeed/docker-project2.git'
                    }
                }
            }
        }
        stage('Installs'){
            steps{
                sh 'ls'
                sh 'cd docker-project2 && pip3 install -r requirements.txt'
            }
        }
        stage('Testing'){
            steps{
                sh 'cd docker-project2 && cd api1 && python3 -m pytest --cov=application'
                sh 'cd docker-project2 && cd api2 && python3 -m pytest --cov=application'
                sh 'cd docker-project2 && cd api3 && python3 -m pytest --cov=application'
                sh 'cd docker-project2 && cd api4 && python3 -m pytest --cov=application'
            }
        }
        stage('Build & Deploy'){
            steps{
                sh 'cd docker-project2 && docker-compose build'
                sh 'cd docker-project2 && docker-compose push'
            }
        }
        stage('Deploy'){
            steps{
                sh 'cd docker-project2 && docker-compose up'
            }
        }
    }
}