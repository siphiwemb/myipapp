pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker-compose build'
      }
    }
    stage('Create Db User') {
      steps {
        sh 'docker-compose up -d mongodb_container'
        sh 'mongo admin < mongo/init.js'
      }
    }
    stage('Test') {
      steps {
        sh 'docker-compose run myipapp python manage.py test'
      }
    }
    stage('Migrate') {
      steps {
        sh 'docker-compose run myipapp python manage.py migrate'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}
