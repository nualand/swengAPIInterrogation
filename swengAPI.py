#  File: swengAPI.py
# by: Nuala Ní Dhomhnaill

from github import Github

# First create a Github instance:

# using username and password
#g = Github("user", "password")

# or using an access token
access_token = "17998201548700064e81c33c95b73e3329973202"
myGithub = Github(access_token)

# prints all my repos
for repo in myGithub.get_user().get_repos():
    print(repo.name)


# prints the contests of a repo
this_repo = "nualand/SoftwareE"
print("The content of " + this_repo)
repo = myGithub.get_repo(this_repo)
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)
