Adapted from:
https://github.com/KalleHallden/ProjectInitializationAutomation

### Pre-setup:
```
Create OS environment variables:
> Desired project base directory as - "mp"
> Github token as - "gt"
  - create new personal access token: https://github.com/settings/tokens
```

### Setup: 
```bash
git clone "https://github.com/jruocco36/GithubMaker.git"
cd GithubMaker
pip install -r requirements.txt

Add "GithubMaker" folder directory to OS system path
```

### Usage:
```
To run the program:

'makeRepo <project_name> <extended directory>'

'<extended directory> is added on to "mp" environment variable

ex:  
   *"mp" = "F:\Documents\Programming Projects"
   > makeRepo GithubMaker /Projects  
   
   Creates a new repository at F:\Documents\Programming Projects\Projects\GitubMaker
```
