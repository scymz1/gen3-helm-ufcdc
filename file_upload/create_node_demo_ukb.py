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
project = "UKB"
node_type = "genomic_profile"

# Load the TSV file
# /home/exouser/cancer_data_commons_ver/genomic_profile_v3.tsv /home/exouser/cancer_data_commons_ver/read_groups_modified.tsv
#  /home/exouser/cancer_data_commons_ver/aliquot_node_modified.tsv
# tsv_file_path = "/home/exouser/cancer_data_commons_ver/genomic_profile_v3.tsv"  # Replace with your TSV file path
# df = pd.read_csv(tsv_file_path, sep="\t")

# Convert dataframe to records
# records = df.to_dict(orient="records")

# tsv_file_paths = ["/home/exouser/cancer_data_commons_ver/samples_modified.tsv", "/home/exouser/cancer_data_commons_ver/slides_modified.tsv", 
# "/home/exouser/cancer_data_commons_ver/slide_image_v3.tsv"]

tsv_file_paths = ["/home/exouser/new_data/UKB/study_ukb.tsv","/home/exouser/new_data/UKB/lab_ukb.tsv", 
"/home/exouser/new_data/UKB/case_ukb.tsv", "/home/exouser/new_data/UKB/core_metadata_collection_ukb_no_id.tsv",
"/home/exouser/new_data/UKB/demographic_ukb.tsv", "/home/exouser/new_data/UKB/follow_up_ukb_drop_duplicate.tsv",
"/home/exouser/new_data/UKB/aliquot_ukb_drop_duplicate.tsv", "/home/exouser/new_data/UKB/molecular_test_ukb.tsv",
"/home/exouser/new_data/UKB/read_group.tsv", "/home/exouser/new_data/UKB/genomic_profile_ukb_v2.tsv"]

# tsv_file_paths = ["/home/exouser/new_data/UKB/genomic_profile_ukb_v2.tsv"]

# Create the nodes
for file in tsv_file_paths:
    response = submission.submit_file(program + "-" + project, file, chunk_size=10)

# Check the response
if response.status_code == 200:
    print(f"Successfully created new node(s) '{node_type}' for program '{program}' and project '{project}'.")
else:
    print(f"Failed to create node(s): {response.status_code} - {response.text}")
