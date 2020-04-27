import sys
import os
from github import Github

# Replace '\' with '/'
# just for looks
for k in range(len(sys.argv)):
    # if k == 0:
    #     continue
    sys.argv[k-1] = sys.argv[k-1].replace('\\','/')

# grab foldername from args, path and Github token from OS user variables
foldername = str(sys.argv[1])
path = os.environ.get('mp').replace('\\','/') # add projects dirctory to the env vars
token = os.environ.get('gt')        # add github token to the env vars

# If extended directory path given (proceeded by '/'), include it in [_dir]
if len(sys.argv) > 2:
    if sys.argv[2][0] == '/':
        _dir = path + str(sys.argv[2]) + '/' + foldername
    else:
        _dir = _dir = path + '/' + foldername
else:
    _dir = _dir = path + '/' + foldername

# Attempt to make new directory for project.
# If directory already exists, get confirmation to 
# proceed and init exisiting directory.
try:
    os.mkdir(_dir)
except FileExistsError:
    print(f'{_dir} already exists...')
    cont = input('Would you like to continue?: ')
    if (cont[0].capitalize()) == 'N':
        print('Quitting...')
        quit()
    
os.chdir(_dir)

# Get github login info from OS user variables and create new repo
g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(foldername, private=True)

# Init repo in local folder and push to newly create Github repo
commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

for c in commands:
    os.system(c)

print(f'{foldername} created locally at {_dir}')
os.system('code .')  # Open new project in VS Code