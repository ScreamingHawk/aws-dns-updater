# aws-dns-updater

A simple script to automatically update an AWS record set to your PCs current publicly facing IP address. 

## Usage

1. [Install and configure boto3](https://boto3.readthedocs.io/en/latest/guide/quickstart.html)
2. [Set up your AWS Hosted Zone](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
3. Run `update_dns.py`
4. Provide the DNS Name and Record Set to update as requested
5. Rejoice!!!
 
## Automate the Script

1. Edit the `update_dns.py` script and hard code the `dns_name` and `record_name` variables
2. Set the program to be run automatically with your favourite task automater (cron/Windows Task Scheduler)
3. Rejoice every 30 minutes!!!

## Who

[Michael Standen](http://michael.standen.link)
