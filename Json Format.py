import requests
import json

def get_azure_instance_metadata():
    # Endpoint URL for Azure Instance Metadata service
    endpoint = "http://169.254.169.254/metadata/instance?api-version=2021-08-01"

    headers = {
        "Metadata": "true"  # Add the "Metadata" header to the request to access the instance metadata
    }

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise an exception if the request was not successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching Azure instance metadata:", str(e))
        return None

if __name__ == "__main__":
    metadata = get_azure_instance_metadata()
    if metadata:
        json_output = json.dumps(metadata, indent=2)  # Convert the metadata to JSON format with indentation
        print(json_output)
