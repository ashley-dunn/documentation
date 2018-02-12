#!/usr/bin/env python3

import os
from optparse import OptionParser
from github import Github, GithubException

ORG_NAME = 'DataDog'
REPO_NAME = 'documentation'


def github_work(options):
    g = Github(options.token)
    try:
        repo = g.get_organization(ORG_NAME).get_repo(REPO_NAME)
        # PR
        response = repo.create_pull(
            title="test translation pr",
            body="translation testing pull request please ignore..",
            base=options.base,
            head=options.head
        )
        print(response)
        print("Done")
        exit(0)

    except GithubException as m:
        print(m)
        exit(1)


def main():
    """
    wrapper for taking cli params
    """
    parser = OptionParser(usage="usage: %prog [options]")
    parser.add_option("-t", "--token", help="auth token")
    parser.add_option("-b", "--base", help="base branch")
    parser.add_option("-d", "--head", help="feature branch")

    (options, args) = parser.parse_args()

    github_work(options)


if __name__ == "__main__":
    main()
