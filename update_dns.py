from json import load
from urllib.request import urlopen
import boto3

dns_name = input("Hosted Zone DNS Name: ")
record_name = input("Record Set Name: ")

my_ip = urlopen('http://ip.42.pl/raw').read().decode('utf-8')
client = boto3.client('route53')
zoneId = client.list_hosted_zones_by_name(DNSName=dns_name)['HostedZones'][0]['Id']
records = client.list_resource_record_sets(HostedZoneId=zoneId)['ResourceRecordSets']
for r in records:
    if r['Name'] == record_name:
        if r['ResourceRecords'][0]['Value'] == my_ip:
            print("IP address {} already matches AWS".format(my_ip))
        else:
            client.change_resource_record_sets(HostedZoneId=zoneId, ChangeBatch={
                'Changes': [{
                    'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': r['Name'],
                            'Type': r['Type'],
                            'TTL': r['TTL'],
                            'ResourceRecords': [{'Value': my_ip}]
                        }
                }]
            })
            print("Updated AWS to IP {}".format(my_ip))

