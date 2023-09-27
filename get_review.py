import sys

from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict):
    authenticator = IAMAuthenticator("NMZMf5sVTPtKFdJcRsvtnei4tsTtHAlMDHEOZfG_8szb")
    service = CloudantV1(authenticator = authenticator)
    service.set_service_url("https://19fd4970-9180-4d9c-8e46-a95087cf83e1-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_find(
        db = "reviews",
        selector = {'dealership': {'$eq': int(dict['id'])}},
        ).get_result()
    try:
        result = {
            'headers':{'Content-Type':'application/json'},
            'body':{'data': response}
        }
        return result
    except:
        return {
            'statusCode': 404,
            'message': 'Something went wrong'
        }
