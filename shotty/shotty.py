# Author Dariush Azimi
# Date Nov 1, 2018
# Print a list of ec2 instances for a project tag (project tag is optional)
# pipenv install pylint --d
# Example:
# pipenv run python shotty/shotty.py --project=spider (in this case
# the project tag is set to spider on the ec2 instances)
import boto3
import click
from datetime import datetime
# import os

session = boto3.Session(profile_name='snapshotty')
ec2 = session.resource('ec2')


def filter_instances(project):
    instances = []
    if project:
        filters = [{'Name': 'tag:Project', 'Values': [project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()
    return instances


@click.group()
def cli():
    """shotty manages snapshots"""


@cli.group('snapshots')
def snapshots():
    """Commands for snapshots"""


@snapshots.command('list')
@click.option('--project', default=None, help="only volumes for project (tag project:<name>)")
def list_snapshots(project):
    '''
    List snapshots 
    '''

    instances= filter_instances(project)
    for i in instances:
        for v in i.volumes.all():
            for s in v.snapshots.all():
                print(', '.join((
                    s.id,
                    v.id,
                    i.id,
                    s.progress,
                    s.start_time.strftime("%c"),
                    s.encrypted and "Encrypted" or "Not Encrypted"
                )))
    return


@cli.group('volumes')
def volumes():
    """Commands for volumes"""

@volumes.command('list')
@click.option('--project', default=None, help="only volumes for project (tag project:<name>)")
def list_volumes(project):
    '''
    List volumes 
    '''

    instances= filter_instances(project)
    for i in instances:
        for v in i.volumes.all():
            print(', '.join((
                v.id,
                i.id,
                v.state,
                str(v.size) + "GiB",
                v.encrypted and "Encrypted" or "Not Encrypted"
            )))
    return


@cli.group('instances')
def instances():
    """ Commands for instances"""


@instances.command('list')
@click.option('--project', default=None, help="only intances for project (tag Project=<name>)")
def list_instances(project):
    '''
    List ec2 instances
    '''
    instances = filter_instances(project)

    for i in instances:
        # if there are no tags, retrun an empty list 'or []'
        tags = {t['Key']: t['Value'] for t in i.tags or []}
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>')
        )))

    return


@instances.command('stop')
@click.option('--project', default=None, help="only instance for project (tag Project=<name>")
def stop_instances(project):
    "Stop Ec2 instances"
    instances = filter_instances(project)
    for i in instances:
        print("Stopping {0}... ".format(i.id))
        i.stop()
    return


@instances.command('start')
@click.option('--project', default=None, help="only instance for project (tag Project=<name>")
def start_instances(project):
    "Start Ec2 instances"
    instances = filter_instances(project)
    for i in instances:
        print("Starting {0}... ".format(i.id))
        i.start()
    return


if __name__ == '__main__':
    cli()
