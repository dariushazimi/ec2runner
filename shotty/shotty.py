# Author Dariush Azimi
# Date Nov 1, 2018
# Print a list of ec2 instances for a project tag (project tag is optional)
# pipenv install pylint --d
# Example:
# pipenv run python shotty/shotty.py --project=spider (in this case
# the project tag is set to spider on the ec2 instances)
import boto3
import click
# import os

session = boto3.Session(profile_name='snapshotty')
ec2 = session.resource('ec2')


@click.command()
@click.option('--project', default=None,
                help="only intances for project (tag Project=<name>)")
def list_instances(project):
    '''
    List ec2 instances
    '''
    if project:
        filters = [{'Name': 'tag:Project', 'Values': [project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
        # if there are no tags, retrun an empty list 'or []'
        tags = { t['Key']: t['Value'] for t in i.tags or []}
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>')
        )))


if __name__ == '__main__':
    list_instances()
