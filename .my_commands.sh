#!/bin/bash

# not fully working
# remote.py not taking second argument
# .env not set up
function create() {
    python "F:\Documents\Programming Projects\Projects\githubMaker\remote.py" $1 $2
    echo $1 $2

    cd
    # source .env
    # python remote.py $1
    cd 'F:\Documents\Programming Projects\'
    # git init
    # git remote add origin git@github.com:$USERNAME/$1.git
#     touch README.md
#     git add .
#     git commit -m "Initial commit"
#     git push -u origin master
#     code .
}