from http.server import BaseHTTPRequestHandler

from aws_cdk.aws_s3 import Bucket

from s3_bucket_model import S3BucketModel
from aws_cdk import App, Environment, Stack


class Controller(BaseHTTPRequestHandler):
    def sync(self, parent, children):

        s3_bucket = S3BucketModel(**parent["metadata"])

        app = App()
        stack = Stack(app, s3_bucket.name)

        # Create an S3 bucket based on the parent's parameters
        Bucket(
            stack,
            f"Bucket{s3_bucket.account_id}{s3_bucket.name}",
            bucket_name=s3_bucket.name
        )

        # Generate the desired CloudFormation template
        cloudformation_template = app.synth().get_stack(stack.stack_name).template

        # Return the CloudFormation template as the desired state
        return {"template": cloudformation_template.to_json()}
