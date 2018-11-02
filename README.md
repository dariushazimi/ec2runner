# aws-snapshot-analyzer
AWS: Manage AWS Ec2 instance snapshots

## About

This project uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile shotty`

## Running

To run the script

`pipenv run python shotty/shotty.py <command> (or start|stop) --project=PROJECTNAME`

`<command>` is the list of commands to run:
-   list   List ec2 instances
-   start  Start Ec2 instances
-   stop   Stop Ec2 instances

Options:
~ --help  Show this message and exit.



Each command has its own help as well.:
`pipenv run python shotty/shotty.py list --help`

Usage:
shotty.py-list [OPTIONS]
List Ec2 instances
Options:

project Dariush Only instances for project (tag Project:Dariush)
help            Only this message and exit.

## Examples - Latest version
 Start instances with taged with project "spider"
```
 pipenv run python shotty/shotty.py start --project=spider
 pipenv run python shotty/shotty.py --help
 pipenv run python shotty/shotty.py instances --help
 pipenv run python shotty/shotty.py instances list --help
 pipenv run python shotty/shotty.py instances stop --help
 pipenv run python shotty/shotty.py instances stop
 pipenv run python shotty/shotty.py instances stop --project=spider
 pipenv run python shotty/shotty.py volumes list
 ```
 