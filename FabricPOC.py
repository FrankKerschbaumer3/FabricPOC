from fabric import Connection
from git import Repo
import os
import shutil
#Local directory.
directory = "./test"
#Checks for current directory.
exists = os.path.isdir(directory)
#SSH github url.
git_url = 'git_url'
#path that is created and then git directory cloned into.
local_path = './test'
#Release version that will be checked out.
release_candidate = input("Enter the Release for Checkout:")
#checks if directory is already created, if so it removes it to be created during git repo clone command.
if exists == True:
    shutil.rmtree(directory)
else:
    pass
#Clones repo into local_path directory.
Repo.clone_from(git_url, local_path, branch=release_candidate)
#Uses Fabric to ssh to host and user specified using default SSH key.
c = Connection(
    host="hostname",
    user="username",
)
#Copies existing deployment file to a backup, puts the new file into deployment
result = c.run("cp file_name.yaml filename_backup.yaml")
result = c.put("./test/file_name",)
result = c.run("ls -asl")