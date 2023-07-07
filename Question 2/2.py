import headers
import json
import requests
import base64

# Convert file to Base64 before sending
with open("file_to_upload.docx", 'rb') as f:
    base64_file = base64.b64encode(f.read())

document_to_upload = {
    "type": "SEC_TRAINING",
    "file": base64_file,
}

# Upload the evidence for the user
response = requests.post(
    f'https://public-api.drata.com/public/users/{user_id}/documents', 
    headers=headers,
    data=json.dumps(document_to_upload)
)
