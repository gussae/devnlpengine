import os
import json
import boto3


os.environ['AWS_REGION'] = 'us-west-2'

payload= {
    "x": 1,
    "y": 2
}

#! Your function name is not the resource name and it is appended with your env : so it's f"{functionName}-{envName}" 
client = boto3.client('lambda')
response = client.invoke(
    FunctionName="nlpengine-test-dev",
    InvocationType="RequestResponse",
    Payload = json.dumps(payload)
)

#uncomment response to identify connection issues
#print(response) 
print(json.load(response['Payload']))
