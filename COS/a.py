import requests

endpoints_url = "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints"
response = requests.get(endpoints_url).json()
print(response)
