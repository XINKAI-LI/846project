import csv
import subprocess
import json
from pydriller import RepositoryMining

# create the project URL list

url_list = []
with open('topJavaMavenProjects.csv') as csv_file:
    i = 0
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if i == 0:
            i += 1
            continue
        url_list.append(row[0])



#  create the base table (cm_pj_usr) where
# key: commit_id
# value: project_info (dic), user_info (dic), bug_num
f = open("sstubs.json")
sstubs = json.load(f)

commit_id_set = set()
for item in sstubs:
    commit_id_set.add(item["fixCommitSHA1"])

cm_pj_usr = {}
for item in sstubs:
    
    project_name = item["projectName"].split(".")[1]
    commit_id = item["fixCommitSHA1"]
    #user_name = subprocess.run(["git", "show", commit_id , "|", "grep", "Author"])
    user_name = "xinkai li" # cannot get it need use pydriller
    #project_url = project_dic[project_name]
    
    #for commit in RepositoryMining(project_url, only_commits=[commit_id]).traverse_commits():
    #    user_name = commit.author.name
    
    pj_usr_name = project_name + " " + user_name
    bug_num = 1
    if commit_id in cm_pj_usr.keys():
        bug_num = cm_pj_usr[commit_id]["bug_num"]
        bug_num += 1
    cm_pj_usr[commit_id] = {
        "project_info": project_name,
        "user_info": pj_usr_name,
        "bug_num": bug_num
        }


# build the project_info table where
# key: project_name
# value: project_info

# build the user_info table where
# key: project_user_names
# value: user_info

# go through the cm_pj_usr table
# use project_name to get project_info
# use pj_usr_name to get user_info
# save data in format (bug_num, project_info, user_info) into a csv
