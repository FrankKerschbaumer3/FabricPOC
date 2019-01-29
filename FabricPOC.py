from fabric import Connection
from git import Repo
import inquirer
import os
import shutil
from patchwork.transfers import rsync
import requests

#Needs GitPython, Fabric, Patchwork, requests installed.
GIT_TOKEN = "access_token1"

server = [
  inquirer.List('server',
                message="Which server do you want to deploy to?",
                choices=['QA', 'PROD'],
            ),
]
answer_of_server = inquirer.prompt(server)
#prints output of server choice
print (answer_of_server['server'])
serverTarget = str(answer_of_server['server'])

#gets repo input then 
repo = [
  inquirer.List('repo',
                message="Which repo are you deploying to?",
                choices=['gitrepo1', 'gitrepo2', 'gitrepo3'],
            ),
]

answer_of_repo = inquirer.prompt(repo)
repoTarget = str(answer_of_repo['repo'])

if repoTarget == 'gitrepo1':
    project = "project_directory1"
if repoTarget == 'gitrepo2':
    project = "project_directory2"
if repoTarget == 'gitrepo3':
    project = "project_directory3"
else:
    exit(0)

git_url = "github_url" + repoTarget + ".git"

directory = "./" + repoTarget

exists = os.path.isdir(directory)
if exists == True:
   shutil.rmtree(directory)
else:
   pass

#prints output of repo choice
answer_of_jira = input('Enter a jira ticket Number:')
print (answer_of_jira)
print ('\n')

#gets release output and assigns it to a global variable
answer_of_release = input('Enter a Release Number, Must be unique and incremental!\nExample: ')
print (answer_of_release)

Repo.clone_from(git_url, project, branch=answer_of_release)
#Uses Fabric to ssh to host and user specified using default SSH key.

if serverTarget == 'PROD':
    c = Connection(
        host="hostname",
        user="user",
    )
if serverTarget == 'QA':
    c = Connection(
        host="hostname",
        user="user",
    )
else:
    exit(0)

rsync(c, source=project, target="to/path", rsync_opts=("--checksum", "--verbose", "--chmod=ug+rwx,o+rx"), exclude=("*.git", "*.md"))