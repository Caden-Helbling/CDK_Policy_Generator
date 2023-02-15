from aws_cdk import core as cdk
import aws_cdk.aws_s3 as s3

import random

num = str(random.randint(0, 1000))

app = cdk.App()            
class HelloCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "cdk-v2-deploy-caden-" + num, versioned=True, removal_policy=cdk.RemovalPolicy.DESTROY)


HelloCdkStack(app, "caden-test-cdk-v2")
app.synth()