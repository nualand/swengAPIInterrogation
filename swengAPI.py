#  File: swengAPI.py
# by: Nuala Ní Dhomhnaill

from github import Github
import csv


# First create a Github instance:

# using username and password
#g = Github("user", "password")

# or using an access token
access_token = "17998201548700064e81c33c95b73e3329973202"
myGithub = Github(access_token)


this_repo = "phadej/github"
repo = myGithub.get_repo(this_repo)
user = myGithub.get_user('phadej')
print (user)
for repo in myGithub.get_user('phadej').get_repos():
    print(repo.name)



    
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
# prints the contests of a repo


print("The content of " + this_repo)
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)

#creating a list of branches from this_repo
the_branches = list(repo.get_branches())
print(*the_branches, sep = "\n")

public_repos = myGithub.get_user().public_repos
print("Number of public repos " + str(public_repos))

private_repos = myGithub.get_user().total_private_repos
print("Number of public repos " + str(private_repos))

number_pulls=0
#    pull_numbers = []
#    pull_titles  = []
#
with open('pull_requests.csv','w',newline = '') as f:
    the_writer = csv.writer(f)
    the_writer.writerow(['Pull Number','Pull Title'])
    pulls = repo.get_pulls(state='open', sort='created', base='master')
    for pr in pulls:
    #    pull_numbers.append(pr.number)
    #    pull_titles.append(pr.title)
     number_pulls = number_pulls+1
     the_writer.writerow([str(pr.number),str(pr.title)])

#    print( pull_numbers)
#    print(pull_titles)


#repo.get_commit(sha=sha).create_status(
#    state="pending",
#    target_url="https://FooCI.com",
#    description="FooCI is building",
#    context="ci/FooCI"
##)
#java = 0
#repositories = myGithub.search_repositories(query='language:java')
#for repo in repositories:
#    java +=1
#    print( java)
#commit = repo.get_commit(sha =sha)
#print(commit.commit.author.date)
