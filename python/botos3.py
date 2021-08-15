import boto3
from botocore.exceptions import ClientError, ParamValidationError

s3=boto3.client("s3", region_name="s-east-1")

def s3_list_buckets():
    try:
        data=s3.list_buckets()
        return data
    except ParamValidationError as e :
        print( f'Param validation Error : {e} ')
    except ClientError as e:
        print(f" Client Error :{e}")

def main():
    print(' Code loaded successfully ')
    response= s3_list_buckets()
    print(' S3. buckets in your Account')
    for bucket in response['Buckets']:
        print(f"{bucket['Name']} ")

if __name__=='__main__':
    main()