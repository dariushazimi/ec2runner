# Author Dariush Azimi
# Date Nov 1, 2018

# pipenv install pylint --d 

import boto3

if __name__ == '__main__':

    session = boto3.Session(profile_name='snapshotty')
    ec2 = session.resource('ec2')
    for i in ec2.instances.all():
        print(i)