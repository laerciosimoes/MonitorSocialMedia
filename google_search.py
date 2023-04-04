from googlesearch import search
import os
import boto3

import datetime

# the query we want to search
queries = ["Laercio Simoes", "Biohacking", "Biohacking.ai"]

s3 = boto3.client('s3')

BUCKET_NAME = "monitor-social-media"


# def lambda_handler(event, context):
for query in queries:
    # perform the search and get the top 20 results
    search_results = search(query, num_results=20)

    now = datetime.datetime.now().strftime("%Y%m%d")

    FILE_NAME = f"{query}-{now}.txt"


    with open(FILE_NAME, "w") as f:
        # write each result to the file
        for url in search_results:
            f.write(url + "\n")

    # upload the file to S3
    s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)

    # delete the file from the Lambda container
    os.remove(FILE_NAME)

    print(f"Search results saved to {BUCKET_NAME}/{FILE_NAME}")

    #return {    'statusCode': 200,     'body': f"Search results saved to {BUCKET_NAME}/{FILE_NAME}"   }

