# AmityMoodleBCP
Amity Moodle Business Continuity

Project Description:
The purpose of this project is to Backup Strategy and Continuity Plan Moodle Amity.

Architecture Diagrams of project
image

image

Steps of project
• Automated files and database backup and transferred to another location. • Notifications Running. • Setup the Template (Custom AMI) • RunServer • Restore Data and Test • Documentation

User stories for BCP-Amity Moodle
Take an informed decision whether to use OpenTofu or Terraform. Decide on the version?
Understand the licensing model and cost.
Come up with a feature matrix supporting what all cloud platforms is supported.
Create a AWS environment for hosting BCP-Amity Moodle’s backup.
Confirmation file to get in all the parameters (e.g.: account, tokens etc..
Create an S3 bucket in the AWS environment.
Configurations related to S3.
Write a shell script or python program that can periodically copy Moodle backup files from hosting heroes to AWS s3.
A python program that will send the email about the summary of back up done.
A python program that will send the email with deletion of old backups as part of summary.
Use poetry (virtual environments) and black (PEP8 compliance) libraries for all python program.
Create a lambda function that can host the python program 5 & 6.
Using open tofu or terraform.
Create a EC2 instance in AWS for hosting Moodle
A terraform or OpenTofu code that will create the needed EC2 instance with memory, cpu and access to the S3 bucket created in step 3.
Span the EC2 instance when it is needed
That will start Moodle
Get the DNS pointed to the initiated Moodle.
Will connect to the recent backup on the s3 bucket.
Costing plan
Cost of S3 bucket.
Cost of lambda function with SENS (Simple Email notification service).
Cost of EC2 instance.
AWS cloud watch and other running cost (e.g. static IP, DNS).
Condition of satisfaction:
Able to get back and cyclic deletion emails to Fazal, Andreas and Prem (to their respective Vallabha accounts).
Able to trigger BCP as needed and able to connect to Moodle from the backup DNS.
