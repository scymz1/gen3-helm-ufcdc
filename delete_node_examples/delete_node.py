from gen3.auth import Gen3Auth
from gen3.submission import Gen3Submission

# Set up the URL of the Gen3 commons you're working with
commons_url = 'https://ufcdc-dev.cis230185.projects.jetstream-cloud.org'

# Authenticate using your credentials file (JSON format)
credentials = "/home/exouser/credentials.json"
auth = Gen3Auth(commons_url, refresh_file=credentials)

# Instantiate the Gen3Submission class to interact with the submission API
submission = Gen3Submission(commons_url, auth)

# Specify the program, project, and the type of node to be deleted
program = "adni"
project = "demo_data_project_adni"
node_type = "demographic"

# Delete the node of type 'demographic' from the specified program and project
response = submission.delete_node(program, project, node_type)

if response.status_code == 200:
    print(f"Successfully deleted node '{node_type}' from program '{program}' and project '{project}'.")
else:
    print(f"Failed to delete node: {response.status_code} - {response.text}")

