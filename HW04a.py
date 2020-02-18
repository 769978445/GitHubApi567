"""SSW567 HW04a
Xiangyu Wang"""

import requests
import json


def get_repo_info(id='769978445'):  # Given a user <ID>
    output = [] # initial output
    user_url = 'https://api.github.com/users/{}/repos'.format(id) # To retrieve a user's list of repositories
    res = requests.get(user_url)
    repos = json.loads(res.text)
    output.append('User: {}'.format(id))

    try:
        repos[0]['name']
    except (TypeError, KeyError, IndexError):
        return 'unable to fetch repos from user' # exception prompts when encountering a bad data

    try:
        for repo in repos:
            repo_name = repo['name']
            # To retrieve the commits for a specific user repository
            repo_url = 'https://api.github.com/repos/{}/{}/commits'.format(id, repo_name)
            repo_info = requests.get(repo_url)
            repo_info_json = json.loads(repo_info.text)
            output.append('Repo: {} Number of commits: {}'.format(repo_name, len(repo_info_json)))
    except (TypeError, KeyError, IndexError):
        return 'unable to fetch commits from repo'

    return output # return a list of JSON objects, one object for each commit.


if __name__ == '__main__':
    for entry in get_repo_info():
        print(entry)