#  File: swengAPI.py
# by: Nuala Ní Dhomhnaill

from github import Github

# First create a Github instance:

# using username and password
#g = Github("user", "password")

# or using an access token
access_token = "17998201548700064e81c33c95b73e3329973202"
myGithub = Github(access_token)


this_repo = "phadej/github"
repo = myGithub.get_repo(this_repo)
# prints the contests of a repo

print("The content of " + this_repo)
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)

#creating a list of branches from this_repo
the_branches = list(repo.get_branches())
print(*the_branches, sep = "\n")

#
#repositories = myGithub.search_repositories(query='language:java')
#for repo in repositories:
#    print(repo)
