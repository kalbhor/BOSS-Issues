from pprint import pprint
import requests

response = requests.get('https://api.github.com/users/coding-blocks/repos').json()

for i in response:
    if int(i['open_issues_count']) > 0:
        r = requests.get('{}/{}'.format(i['url'],'issues'))
        print(r.text)
