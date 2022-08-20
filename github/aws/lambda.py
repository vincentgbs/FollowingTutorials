## CFT Setup Notes:
## Must add Lambda Layer with Git https://github.com/lambci/git-lambda-layer
## Must create IAM role with SSMReadOnlyAccess
## Must create Github Personal Access Token and add it to Parameter Store
## https://github.com/settings/tokens/new

import boto3
import subprocess
import os

def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    password = ssm.get_parameter(Name='github/password', WithDecryption=True)
    password = password['Parameter']['Value']

    os.chdir('/tmp') ## for Lambda write permissions
    scriptname = 'script.sh'
    f = open(scriptname, 'a')
    f.write(f"git clone https://{password}@github.com/vincentgbs/FollowingTutorials.git")
    f.write("cd FollowingTutorials/github")
    f.write("./github.sh")
    f.close()
    os.chmod(scriptname, 0o700)
    subprocess.call(['sh', scriptname])
    os.remove(scriptname) ## clean up
