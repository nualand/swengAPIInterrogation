#  File: swengAPI.py
# by: Nuala Ní Dhomhnaill

from github import Github
import csv


# create a Github instance using access token:

access_token = "17998201548700064e81c33c95b73e3329973202"
myGithub = Github(access_token)


#going to be interrogating this users github
user = myGithub.get_user('abhishekbanthia')




def count_pulls(repo):
    number_pulls = 0
    pulls = repo.get_pulls(state='open', sort='created', base='master')
    for pr in pulls:
        number_pulls = number_pulls+1

    return number_pulls


#print("The content of " + this_repo)
#contents = repo.get_contents("")
#for content_file in contents:
#    print(content_file)



public_repos = myGithub.get_user().public_repos
print("Number of public repos " + str(public_repos))

private_repos = myGithub.get_user().total_private_repos
print("Number of public repos " + str(private_repos))

number_pulls = 0
number_favourites = 0
repo_id=1
num_repo = 0

# writing of csv files

with open('csv/repostitory_info.csv','w',newline = '') as a_file:
    the_writer = csv.writer(a_file)
    the_writer.writerow(['Repository Number','Repository Name','Number of Pulls','Number of Stars'])
    for repo in myGithub.get_user(user.login).get_repos():
        stars_count =  repo.stargazers_count
        number_pulls = count_pulls(repo)
    #    number_favourites = count_favourites(repo)
        the_writer.writerow([repo_id,repo.name,number_pulls,stars_count])
        repo_id += 1
        num_repo +=1

with open('csv/user_infor.csv','w',newline = '') as file:
    the_user_writer = csv.writer(file)
    the_user_writer.writerow(['Username','Name','Number of Repos'])
    the_user_writer.writerow([user.name,user.login,num_repo])
