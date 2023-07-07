To find out which personnel haven't completed training yet, you execute a GET request on the /public/personnel endpoint and specify the securityTrainingCompliance filter as "false". See 1.py for more info. Sample output below;

Sample JSON output:
{
    "id": 1,
    "firstName": "John",
    "lastName": "Doe",
    "email": "johndoe@example.com",
    "employmentStatus": "CURRENT_EMPLOYEE",
    "securityTrainingCompliance": false,
}
