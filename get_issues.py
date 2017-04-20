"""
    To fetch all issues of coding-blocks repos with label 'BOSS'
    - Optional authentication
"""

import requests

from requests.auth import HTTPBasicAuth

def getIssuesWithLabel(username='', password='', label='BOSS'):
    """
        Returns issues of coding-blocks repos with label
    """
    issuesResult = []

    # User authentication if username is provided
    auth = HTTPBasicAuth(username, password) if len(username) else None
    repos = requests.get(
        'https://api.github.com/users/coding-blocks/repos',
        auth=auth
        ).json()

    for repo in repos:
        if int(repo['open_issues_count']) > 0: # Check if repo has open issues
            issues = requests.get(
                '{}/{}'.format(repo['url'], 'issues'),
                params={label: label},
                auth=auth
                ).json() # Get repo issues

            for issue in issues:
                issue['repo'] = repo
                issuesResult.append(issue)

    return issuesResult

# Use github authentication since we get only 60 API requests
# with unauthenticated requests

"""
Usage: 
import getpass

username = raw_input("Enter github username: ")
password = getpass.getpass("Enter password: ")

issues = getIssuesWithLabel(username, password)
for issue in issues:
    print issue['repo']['name'] + " : " + issue['title']

"""