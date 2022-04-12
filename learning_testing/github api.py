# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:04:49 2019

@author: jaredalbert
"""
#
from collections import namedtuple
import os
from gist_token import gist_token
from github import Github, InputFileContent
'''
#r = namedtuple('cat','name color temperment')
#sylvia = r('sylvia','blue','mean')
#print(sylvia)'''
testing = 'test'
gh = Github()
Repo = namedtuple('Repo', 'name stars forks')


pb = gh.get_user('pybites')


def get_repo_stats(user, n=5):
    repos = []
    for repo in user.get_repos():
        if repo.fork:
            continue

        repos.append(Repo(name=repo.name,
                          stars=repo.stargazers_count,
                          forks=repo.forks_count))
    return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]


print(get_repo_stats(pb, n=5))
token = gist_token()

gh = Github(token)
me = gh.get_user()
me.create_gist(True,{"repo_stats.py":InputFileContent(testing)}, 'test' )
