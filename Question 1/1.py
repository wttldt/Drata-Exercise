import requests
import json

# Your Drata API key here
API_KEY = 'your_drata_api_key_here'
headers = {'Authorization': f'Bearer {API_KEY}'}

parameters = {
    'securityTrainingCompliance': 'false',
}

response = requests.get('https://public-api.drata.com/public/personnel', headers=headers, params=parameters)

# Print out personnel who haven't completed training yet
if response.status_code == 200:
    json_data = json.loads(response.text)
    for person in json_data['data']:
        print(person)
