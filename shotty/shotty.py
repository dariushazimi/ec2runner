# Author Dariush Azimi
# Date Nov 1, 2018

# pipenv install pylint --d 

import boto3
import click
# import os

session = boto3.Session(profile_name='snapshotty')
ec2 = session.resource('ec2')


@click.command()
def list_instances():
    '''
    List Ec2 instances
    '''
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name
        )))


if __name__ == '__main__':
    # print(sys.argv)

    list_instances()
