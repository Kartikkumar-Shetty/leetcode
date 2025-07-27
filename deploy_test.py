import json
import subprocess
import os
import boto3
import requests



def get_secretData(SecretID):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=SecretID)
    return list(json.loads(response['SecretString']).values())
    
try:
    path = "/tmp/"
    package_name = os.environ['PackageName']
    secretID = os.environ['ArtifactoryCred']
    artifactory_url = os.environ['ArtifactoryUrl']
    repo_name = os.environ['ArtifactoryRepo']
    user,passwd = get_secretData(secretID)
    auth_values = (user, passwd)
    auth_string = user + ":" + passwd
except:
    print("Variables not present")
    
def api_result(payload):
    api_url = "https://artifactory.connectwisedev.com/artifactory/api/search/aql"
    api_response = requests.post(api_url, data=payload, auth=auth_values)
    obj = api_response.json()
    return obj

def upload_package(s3_details):
    s3 = boto3.client('s3')
    package_path = "{0}/{1}/{2}/{3}".format(s3_details['vendor_name'],s3_details['product_name'],s3_details['build_version'],package_name) 
    art_path = "{0}_{1}/{2}".format(s3_details['vendor_name'],s3_details['product_name'],s3_details['build_version'])
    upload_path = "{0}/{1}/{2}/{3}".format(artifactory_url,repo_name,art_path,package_name)
    query = 'items.find({"repo":{"$eq":"'+repo_name+'"}},{"$and":[{"path":{"$match":"'+art_path+'"}}]})'
    response = api_result(query)
    if len(response['results']) == 0:
        s3.download_file(s3_details['bucket_name'], package_path, path + package_name)
        # cmd = ['curl', '-u', auth_string, '-X', 'PUT', upload_path , '-T', path + package_name]
        # subprocess.run(cmd)
        try:
            uid_pass = auth_string.split(":")
            with open(path + package_name, 'rb') as f:
                response = requests.put(upload_path, data=f, auth=(uid_pass[0], uid_pass[1]))
            print("File upload operation dine with status code:" + response.status_code + " and response: " + response.text)
        except Exception as e:
            print(f"An error occurred while uploading file to artifactory: {e}")        
    else:  
        print("build_version={0} | vendor_name={1} | product_name={2} -- already exist".format(s3_details['build_version'],s3_details['vendor_name'],s3_details['product_name']))

def package_actions(s3_details):
    s3 = boto3.client('s3')
    data = s3.get_object(Bucket=s3_details['bucket_name'], Key=s3_details['file_path'])
    contents = data['Body'].read()
    promotion_status = str(contents.decode("utf-8")).lower().strip()
    if promotion_status == "review-requested" or promotion_status == "qa-ready":
        upload_package(s3_details)
        
def init(event):
    file_path = event['Records'][0]['s3']['object']['key']
    s3_bucket_name = event['Records'][0]['s3']['bucket']['name']
    build_data = file_path.split("/")
    
    s3_Details = {
        "bucket_name": s3_bucket_name,
        "file_path": file_path,
        "vendor_name": build_data[0],
        "product_name": build_data[1],
        "build_version": build_data[2]
    }

    return s3_Details
    
def lambda_handler(event, context):
    print(event)
    s3_details = init(event)
    if s3_details["vendor_name"].startswith("REF_Automation_") or s3_details["vendor_name"].startswith("REF_INTERNAL_"):
        return "skip package actions as this is test vendor"
    package_actions(s3_details)
    return "complate"
