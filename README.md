# p.ai

## Prerequisite software

1. [Git](https://git-scm.com/downloads), choose right version
2. Python 3.6.2

## Phase 0

1. Scrape disease data and QA data from __(website?)__ and store them in csv files
2. Research on keywords extraction/generation and disease match models and document it in a word file


## Phase 1
1. Build a simple application demo 


## How to set up `Flask` environment

We are choosing `Flask` as our web framework to build the first version of application, and use `virtualenv` to create isolated Python environment so it won't affect other projects locally. 

After checking out code, 

1. Follow this [link](https://virtualenv.pypa.io/en/stable/installation/) to install `virtualenv`
2. Activate environment by `.\vevn\Scripts\activate`
3. Deactivate environment using `deactivate`

After activating environment, to run `Flask`

```
>set FLASK_APP=./test/test.py
>flask run
```

## File share/Code commit
Requester:
1. Fork cs3285/p.ai to your own github account, copy _HTTPS_ URL. For example, mine is https://github.com/zchi1992/p.ai.git
2. Open Git Bash, change directory to where you want to clone the project. For example, `cd d:`
3. `git clone (URL)` to your local directory
4. After files are changed, commit to your __forked__ github repo
5. In 'Pull requests' tab, click 'New pull request' and review changes
6. Click 'Create pull request', add comments and click 'Create pull request'

Owner:

1. When receiving a new pull request, click 'Pull requests' tab in project repo
2. Review changes. If it is okay, click 'Merge pull request'. 
3. If it is not okay, add comments.

_Note_: after clicking 'Merge pull request', the change will merge to `master` branch. So carefully review the change before merging.

# Git

[fork from a remote repo](https://help.github.com/articles/syncing-a-fork/)

abcd