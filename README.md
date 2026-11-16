# Automated ETL Pipeline Using AWS

## Week 4 AWS Cloud Project

**Prepared by:** Cana Tshibanda

## 1. Project Overview

For this project, I worked on creating an automated ETL pipeline using AWS. The aim was to take sales data from a CSV file, process it and save the updated information in another S3 bucket.

I used different AWS services to make the process happen automatically instead of having to process the file manually.

## 2. AWS Services I Used

- **Amazon S3:** I created two buckets to store the original and processed CSV files.
- **AWS Lambda:** I used Lambda to run my Python code and process the sales data.
- **AWS IAM:** I configured permissions so that Lambda could read and save files in the S3 buckets.
- **Amazon CloudWatch:** I used CloudWatch to check the Lambda execution logs and see if the function ran successfully.

## 3. How I Built the Pipeline

1. I created two S3 buckets, one for the original data and another for the processed data.
2. I created a CSV file containing sample sales transactions and uploaded it to the raw data bucket.
3. I created a Lambda function using Python.
4. I added code to read the CSV file, clean the data and calculate the total for each transaction.
5. I gave the Lambda function permission to access both S3 buckets.
6. I configured an S3 trigger so that the function would run automatically when a CSV file was uploaded.
7. I uploaded the CSV file again to test the pipeline.
8. I checked the processed bucket and confirmed that the new CSV file had been created.
9. I also checked CloudWatch logs to monitor the Lambda execution.

## 4. S3 Bucket Details

**Raw data bucket:** `cana-week4-raw-data-2026`

**Processed data bucket:** `cana-week4-processed-data-2026`

## 5. Testing and Results

After uploading the CSV file to the raw data bucket, the S3 trigger activated the Lambda function.

The function processed the sales information and calculated the total amount for each transaction using the quantity and unit price.

I checked the processed S3 bucket and confirmed that the new CSV file was saved inside the `processed` folder. The new file also contained an additional column called `total`.

I used CloudWatch logs to check the Lambda execution.

## 6. Key Learning Outcomes

Through this project, I learned how to:

- Create and manage S3 buckets.
- Create a Lambda function using Python.
- Work with CSV files and process data.
- Connect S3 to Lambda using event triggers.
- Set up IAM permissions for AWS services.
- Save processed files to another S3 bucket.
- Use CloudWatch to monitor Lambda executions.

## 7. Screenshots

I have included screenshots in the `screenshots` folder to show the different stages of the project, including the S3 buckets, Lambda setup, permissions
