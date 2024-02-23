import os
import sys
import json
import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

#get token from .env file
token = os.getenv('AUTH_TOKEN') 

BASE_URL = 'https://chat.openai.com/backend-api/gizmos/'
HEADERS = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',#need these two headers or get error
    'Te': 'trailers'
}

def getActionsSpec(gptID, dir_path):
    url = BASE_URL + gptID
    response = requests.get(url, headers=HEADERS)

    openai_spec = None
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()

            with open(os.path.join(dir_path, 'FullResponse.json'), 'w') as file:
                json.dump(data, file)

            # loop through the tools and find if it has the 'plugins_prototype' tool 
            # which contains the openai_spec,if not it doesn't have actions
            for tool in data['tools']:
                # Check if the 'type' key equals "plugins_prototype"
                if tool['type'] == "plugins_prototype":
                    # Get the 'openai_spec' of the tool
                    openai_spec = tool['metadata']['raw_spec']

                    # Parse the 'openai_spec' into a Python dictionary
                    openai_spec = json.loads(openai_spec)

                else: 
                    return openai_spec
        
            # Parse the openai_spec into a Python dictionary
            openai_spec = json.loads(openai_spec)

            # Write the openai_spec to a JSON file
            with open(os.path.join(dir_path, 'raw_spec.json'), 'w') as file:
                json.dump(openai_spec, file)

        except (KeyError, IndexError, json.JSONDecodeError) as e:
            print("Error parsing JSON or accessing the data:", e)
    else:
        print("Failed to fetch data. Status Code:", response.status_code)
    
    return openai_spec

def generate_api_requests(openai_spec, dir_path):
    api_requests = []

    base_url = openai_spec['servers'][0]['url']
    paths = openai_spec['paths']

    for path, methods in paths.items():
        for method, details in methods.items():
            api_request = {
                "method": method.upper(),
                "path": path,
                "url": f"{base_url}{path}",
                "content_type": "application/json"
            }

            # Check if request body is required and generate a sample request body
            if 'requestBody' in details:
                content = details['requestBody']['content']
                if 'application/json' in content:
                    schema = content['application/json']['schema']
                    example_body = {}
                    if '$ref' in schema:
                        ref = schema['$ref'].split('/')[-1]
                        properties = openai_spec['components']['schemas'][ref]['properties']
                        for prop, prop_details in properties.items():
                            example_body[prop] = f"<{prop_details.get('type', 'value')}>"
                    api_request["example_body"] = example_body

            # Generate the full request
            full_request = f"{api_request['method']} {api_request['url']} HTTP/2\nContent-Type: {api_request['content_type']}\n\n"
            if "example_body" in api_request:
                full_request += json.dumps(api_request["example_body"], indent=4)
                print(full_request)
            api_request["full_request"] = full_request

            api_requests.append(api_request)

    # Write the api_requests to a JSON file
    with open(os.path.join(dir_path, 'api_requests.json'), 'w') as file:
        json.dump(api_requests, file, indent=4)

def main():

    if len(sys.argv) != 3:
        print("Usage: python GetActions.py <openai GPT ID> <directory name>")
        sys.exit(1)

    gptID = sys.argv[1]  # Get the file path from command line arguments
    directory_name = sys.argv[2]

    #get the a directory up from this folder
    root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    full_dir_path = os.path.join(root_dir, directory_name)

    # Check if the directory exists, if not, create it
    if not os.path.exists(full_dir_path):
        os.makedirs(full_dir_path)

    openai_spec = getActionsSpec(gptID, full_dir_path)
    if(openai_spec == None):
        #get the name of the gpt and remove the id
        gpt_name = gptID[12:].replace('-', ' ')

        print(f"This GPT: '{gpt_name}' doesn't have an openai_spec")
        sys.exit(1)
    generate_api_requests(openai_spec, full_dir_path)

if __name__ == "__main__":
    main()