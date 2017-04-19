import requests
import sys
import getpass
from requests.auth import HTTPBasicAuth


def getIssuesWithLabel(username, password, label='BOSS'):
    repos = requests.get('https://api.github.com/users/coding-blocks/repos', auth=HTTPBasicAuth(username, password)).json()
    bossIssues = []
    
    for repo in repos:
        if int(repo['open_issues_count']) > 0:
            issues = requests.get('{}/{}'.format(repo['url'], 'issues')).json()
    
            for issue in issues:
                labels = [label['name'] for label in issue['labels']]
                if 'BOSS' in labels:
                    issue['repo'] = repo
                    
                    bossIssues.append(issue)
                    
    return bossIssues

# Use github authentication since we get only 60 API requests
# with unauthenticated requests

username = raw_input("Enter github username: ")
password = getpass.getpass("Enter password: ")

issues = getIssuesWithLabel(username, password)
for issue in issues:
    print(issue['repo']['name'] + " : " + issue['title'])
