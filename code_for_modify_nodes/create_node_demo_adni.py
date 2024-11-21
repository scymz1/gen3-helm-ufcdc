from gen3.auth import Gen3Auth
from gen3.submission import Gen3Submission
import pandas as pd

# Set up the URL of the Gen3 commons you're working with
commons_url = 'https://ufcdc-portal.org'

# Authenticate using your credentials file (JSON format)
credentials = "/home/exouser/credentials.json"
auth = Gen3Auth(commons_url, refresh_file=credentials)

# Instantiate the Gen3Submission class to interact with the submission API
submission = Gen3Submission(commons_url, auth)

# Specify the program, project, and the type of node to be uploaded
program = "Project"
project = "ADNI"
node_type = "genomic_profile"

# tsv_file_paths = ["/home/exouser/new_data/ADNI/v2/molecular_test_adni_v2.tsv"]

tsv_file_paths = ["/home/exouser/new_data/ADNI/study_adni.tsv", "/home/exouser/new_data/ADNI/lab_adni.tsv", "/home/exouser/new_data/ADNI/v2/case_adni_v2.tsv",
"/home/exouser/new_data/ADNI/core_metadata_collection_adni.tsv",
"/home/exouser/new_data/ADNI/v2/demographic_adni_v2.tsv", "/home/exouser/new_data/ADNI/v2/follow_up_adni_v2_drop_duplicate.tsv", "/home/exouser/new_data/ADNI/v2/aliquot_adni_v2_drop_duplicate.tsv",
"/home/exouser/new_data/ADNI/v2/molecular_test_adni_v2_drop_duplicate.tsv", "/home/exouser/new_data/ADNI/read_groups_modified.tsv", "/home/exouser/new_data/ADNI/genomic_profile_adni_v2.tsv"]

# tsv_file_paths = ["/home/exouser/new_data/ADNI/v2/molecular_test_adni_v3.tsv"]

# Create the nodes
for file in tsv_file_paths:
    print("upload file:", file)
    response = submission.submit_file(program + "-" + project, file, chunk_size=10)

# Check the response
if response.status_code == 200:
    print(f"Successfully created new node(s) '{node_type}' for program '{program}' and project '{project}'.")
else:
    print(f"Failed to create node(s): {response.status_code} - {response.text}")
