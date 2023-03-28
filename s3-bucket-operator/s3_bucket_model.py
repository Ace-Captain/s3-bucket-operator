from pydantic import BaseModel


class S3BucketModel(BaseModel):
    account_id: string
    name: string
    region: string
