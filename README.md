# 846project

## Train data format

y: Sstubs num

x:
  commit_id (ignore in trainning, but critial to extract all contributor, project, commit information)
  project_related_info: ...
  contributor_related_info: ...
  commit_related_info: ...
  
save in a csv file and each row is corresponding with one x and y.

## File

100 Java Maven Project SStuBs sstubs.json

the name and URL for these 100 projects are in topJavaMavenProjects.csv
