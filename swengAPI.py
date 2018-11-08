#  File: swengAPI.py
# by: Nuala Ní Dhomhnaill

from github import Github

# First create a Github instance:

# using username and password
g = Github("user", "password")

# or using an access token
access_token = "17998201548700064e81c33c95b73e3329973202"
g = Github(access_token)

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token=access_token)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
