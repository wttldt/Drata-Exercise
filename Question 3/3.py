import requests

headers = {"Authorization": "Bearer <YOUR_API_KEY_HERE>"}

workspaceId = "YOUR_WORKSPACE_ID"
testId = "43"
response = requests.post(f"https://public-api.drata.com/public/workspaces/{workspaceId}/autopilot/{testId}/retest", headers=headers)
data = response.json()

# If returned status code is 201 which means the request was successfully received and the test is running
if response.status_code == 201:
    print('Test 43 triggered successfully')
else:
    print('Error triggering test 43')