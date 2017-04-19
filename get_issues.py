from pprint import pprint
import requests

response = requests.get('https://api.github.com/users/coding-blocks/repos').json()

for i in response:
    if int(i['open_issues_count']) > 0: # Check if repo has open issues
        r = requests.get('{}/{}'.format(i['url'],'issues')).json() # Get repos issues
        for j in r:
            print(j['url'])
