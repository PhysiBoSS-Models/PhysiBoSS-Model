import os
short_name = ""
dirs = [dir for dir in os.listdir("sample_projects")  if os.path.isdir(dir) and dir != "template_BM"]
if dirs == 1:
    short_name = dirs[0]
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'model_short_name={short_name}', file=fh)