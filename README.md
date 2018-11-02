# awsbutler 2018

Build with :heart:
AWS: Manage AWS Ec2 instance snapshots, start and stop instances, display the list of instances along with volumes and snapshots.

## About:pencil2:

This project uses boto3 to manage AWS EC2 instance snapshots.

## Configuring :wrench:

awsbutler uses the configuration file created by the AWS cli. e.g.

`aws configure --profile awsbutler`

## Running :rocket:

To run the script

`pipenv run python awsbutler/awsbutler.py <command> <subcommand>--project=PROJECTNAME`

*command* is instances, volumes, or snapshots
*subcommand*  - depends on the command
*project* is optional 

the list of commands to run:
-   list   List ec2 instances
-   start  Start Ec2 instances
-   stop   Stop Ec2 instances

Options:
~ --help  Show this message and exit.



Each command has its own help as well.:
`pipenv run python awsbutler/awsbutler.py list --help`

Usage:
awsbutler.py-list [OPTIONS]
List Ec2 instances
Options:

project Dariush Only instances for project (tag Project:Dariush)
help            Only this message and exit.

## Examples - Latest version
 Start instances with taged with project "spider"
```
 pipenv run python awsbutler/awsbutler.py start --project=spider
 pipenv run python awsbutler/awsbutler.py --help
 pipenv run python awsbutler/awsbutler.py instances --help
 pipenv run python awsbutler/awsbutler.py instances list --help
 pipenv run python awsbutler/awsbutler.py instances stop --help
 pipenv run python awsbutler/awsbutler.py instances stop
 pipenv run python awsbutler/awsbutler.py instances stop --project=spider
 pipenv run python awsbutler/awsbutler.py volumes list

 ```

 #### :rotating_light:Update: List ec2 snapshots with volumes:rotating_light:

  ```
  pipenv run python awsbutler/awsbutler.py snapshots list
  ```
  Output:
```  
snap-008d7, vol-06ffb, i-09e2b, 100%, Fri Nov  2 02:31:11 2018, Not Encrypted
```

### Instance Lifecycle

![aws instance lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/instance_lifecycle.png)

### Note: 
boto3 list the snapshots in chronological order with the most recent one at the top.

The latest commit will show the most recent sussessful snap
```
pipenv run python awsbutler/awsbutler.py snapshots list
pipenv run python awsbutler/awsbutler.py snapshots list --all
pipenv run python awsbutler/awsbutler.py instances snapshot
pipenv run python awsbutler/awsbutler.py snapshots list --help
```
More updates to come.

code is never finished only abandoned :art: