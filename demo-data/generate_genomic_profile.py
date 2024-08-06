import pandas as pd
import random
import string
import os
import hashlib

def generate_random_md5():
    # Generate a random 128-bit (16 bytes) value
    random_bytes = os.urandom(16)  # 16 bytes * 8 bits/byte = 128 bits

    # Compute the MD5 hash of the random bytes
    md5_hash = hashlib.md5(random_bytes).hexdigest()

    return md5_hash

def generate_random_data_category():
    categories = [
        "Combined Nucleotide Variation",
        "Genomic Profiling"
    ]
    return random.choice(categories)

def generate_random_data_format():
    categories = [
        "MAF",
        "VCF",
        "XML",
        "TSV"
    ]
    return random.choice(categories)

def generate_random_data_type():
    categories = [
        "FoundationOne Report",
        "GENIE Report",
        "Raw CGI Variant"
    ]
    return random.choice(categories)

def generate_random_experimental_strategy():
    categories = [
        "ATAC-Seq",
        "Bisulfite-Seq",
        "ChIP-Seq",
        "miRNA-Seq",
        "RNA-Seq",
        "Targeted Sequencing",
        "WGS",
        "WXS"
    ]
    return random.choice(categories)

def generate_random_filename(extension="", length=8):
    # Generate a random string of specified length
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    # Combine the random string with the provided extension
    filename = random_string
    if extension:
        filename += f".{extension}"
    return filename

def generate_random_filesize(min_size=1024, max_size=1048576):
    """
    Generate a random file size within the specified range.

    Args:
        min_size (int): Minimum file size in bytes (default is 1 KB).
        max_size (int): Maximum file size in bytes (default is 1 MB).

    Returns:
        int: A random file size in bytes.
    """
    return random.randint(min_size, max_size)

def generate_random_submitter_id():
    # Generate the random parts of the submitter_id
    random_number = random.randint(10000, 99999)
    clinical = "clinical"
    random_suffix = random.randint(10, 99)
    
    # Combine the parts into the final submitter_id
    submitter_id = f"{random_number}_{clinical}_{random_suffix}"
    
    return submitter_id


# Read the TSV file
df = pd.read_csv('/Users/minghao.zhou/Desktop/gen3/cancer_data_commons_ver/submission_submitted_genomic_profile_template.tsv', sep='\t')
df_meta_data = pd.read_csv('/Users/minghao.zhou/Desktop/gen3/cancer_data_commons_ver/core_metadata_collection_modified.tsv', sep='\t')
df['project_id'] = df['project_id'].astype(object)
df.at[0, "project_id"] = "cancer_commons_program-demo_data_project"
first_row = df.iloc[0]
additional_rows = pd.DataFrame([first_row] * 901, columns=df.columns)

df = pd.concat([df, additional_rows], ignore_index=True)

df['*submitter_id'] = df['*submitter_id'].apply(
    lambda x: generate_random_submitter_id() if pd.isna(x) else x
)

df['*data_category'] = df['*data_category'].apply(
    lambda x: generate_random_data_category() if pd.isna(x) else x
)

df['*read_groups.submitter_id'] = df['*read_groups.submitter_id'].apply(
    lambda x: "read_group_0"
)

df['*md5sum'] = df['*md5sum'].apply(
    lambda x: generate_random_md5() if pd.isna(x) else x
)

df['*file_size'] = df['*file_size'].apply(
    lambda x: generate_random_filesize(min_size=1024, max_size=1048576) if pd.isna(x) else x
)

df['*file_name'] = df['*file_name'].apply(
    lambda x: generate_random_filename(extension="tsv", length=12) if pd.isna(x) else x
)

df['*experimental_strategy'] = df['*experimental_strategy'].apply(
    lambda x: generate_random_experimental_strategy() if pd.isna(x) else x
)

df['*data_type'] = df['*data_type'].apply(
    lambda x: generate_random_data_type() if pd.isna(x) else x
)

df['*data_format'] = df['*data_format'].apply(
    lambda x: generate_random_data_format() if pd.isna(x) else x
)

df['core_metadata_collections.submitter_id'] = df_meta_data['submitter_id']

# print(df.columns)
df = df.drop(columns=['urls'])

# print(df.head(5))
df.to_csv('genomic_profile.tsv', sep='\t', index=False)

# {
#   "type": "rna_expression_calling_workflow",
#   "workflow_type": "CellRanger - 10x Filtered Counts",
#   "submitter_id": "vdagdfhfhan",
#   "workflow_link": "https://github.com/reanahub/reana-workflow-engine-cwl"
# }