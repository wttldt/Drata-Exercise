Once you find out which personnel haven't completed the training, you can use Drata's POST /public/users/{id}/documents endpoint to upload evidence. Here is an example request:

Sample JSON output:
{
    "id": 1,
    "name": "Security Training",
    "type": "SEC_TRAINING",
    "fileUrl": "http://localhost:5000/download/documents/1",
    "createdAt": "2020-07-06 12:00:00.000000",
    "updatedAt": "2020-07-06 12:00:00.000000"
}
