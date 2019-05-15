def bucket = 'lambda-deployment-packages-itikhonov'
def functionName = 'account_public_endpoints'
def region = 'us-east-1'

node {
    stage('Checkout'){
        checkout scm
    }


    stage('Build'){
        sh "cd code && zip -r ../${commitID()}.zip *"

    }

    stage('Push'){
        sh "aws s3 cp ${commitID()}.zip s3://${bucket}"
    }

    stage('Deploy'){
        sh "aws lambda update-function-code --function-name ${functionName} \
                --s3-bucket ${bucket} \
                --s3-key ${commitID()}.zip \
                --region ${region}"
    }

    if (env.BRANCH_NAME == 'master') {
        stage('Publish') {
            def lambdaVersion = sh(
                script: "aws lambda publish-version --function-name ${functionName} --region ${region} | jq -r '.Version'",
                returnStdout: true
            )
            sh "aws lambda update-alias --function-name ${functionName} --name prod --region ${region} --function-version ${lambdaVersion}"
        }
    }

    if (env.BRANCH_NAME == 'staging') {
        stage('Publish') {
            def lambdaVersion = sh(
                script: "aws lambda publish-version --function-name ${functionName} --region ${region} | jq -r '.Version'",
                returnStdout: true
            )
            sh "aws lambda update-alias --function-name ${functionName} --name staging --region ${region} --function-version ${lambdaVersion}"
        }
    }
}



def commitID() {
    sh 'ls -alh .git'
    sh 'git rev-parse HEAD > .git/commitID'
    def commitID = readFile('.git/commitID').trim()
    sh 'rm .git/commitID'
    commitID
}
