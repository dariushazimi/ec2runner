from setuptools import setup

setup(
    name="awsbutler-2018",
    version="2018-11-01-0.1",
    author="Dariush Azimi",
    author_email="azimid@gmail.com",
    description="awsbutler-2018 is a tool to manage AWS EC2 snapshots, list,stop,start intances and show related volumes",
    license="GPLv3+",
    packages=['awsbutler'],
    url="https://github.com/dariushazimi/aws-snapshot-analyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        awsbutler=awsbutler.awsbutler:cli
        '''

)