pipeline {
    agent { docker { image 'node:26.13.0-alpine3.24' } }
    stages {
        stage('build') {
            steps {
                sh 'node --version'
            }
        }
    }
}
