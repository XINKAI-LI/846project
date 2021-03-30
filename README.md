# 846project

## Train data metrixs

y: Sstubs num

x:
  commit_id (ignore in trainning, but critial to extract all contributor, project, commit information)
  project_related_info: ...
  contributor_related_info: ...
  commit_related_info: ...
  
save in a csv file and each row is corresponding with one x and y.

## data_extract

How to extract data with current tool is the challenge.

**step1:**
build the (commit_id: commit_info, project_name, contributor_name) table

Pydriller:

for each project: \
  for each commit: (apply filter to select these commits with Sstubs) \
    get commit info \
    save (commit_id, commit_info, project_name, contributor_name)

**step2:**
build the (project-name: project info) table

**step3:**
build the (contributor-name: contributor info) table

**step4:**
build the final train-table

for item in step1-table:
  project_related_info = extarct info from proejct-table by item.project_name \
  contributor_related_info = extarct info from contributor-table by item.contributor_name \
  commit_related_info = item.commit_info \
  Sstubs_num = item.commit_info.bug_num \
  save(commit_related_info, contributor_related_info, project_related_info, Sstubs_num) into train-table

**step5:** \
data pre-process \
normalize, or catergorize each column.

## Data analysis


## Model build


## File

100 Java Maven Project SStuBs sstubs.json

the name and URL for these 100 projects are in topJavaMavenProjects.csv
