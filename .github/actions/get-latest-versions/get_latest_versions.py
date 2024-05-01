import requests
import os

headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {os.environ["GITHUB_API_TOKEN"]}'}

tre_repositories = ['da-tre-fn-dlq-slack-alerts',
                    'da-tre-fn-process-monitoring-queue',
                    'da-tre-fn-slack-notifications',
                    'da-tre-fn-court-document-packer',
                    'da-tre-fn-sqs-sf-trigger',
                    'da-tre-fn-court-document-pre-parser',
                    'da-tre-fn-court-document-pre-packer',
                    'da-tre-fn-failure-destination',
                    'da-tre-fn-success-destination',
                    'da-tre-fn-vb-bag-validation',
                    'da-tre-fn-vb-bag-files-validation'
                    ]


def url(repo):
    return f"https://api.github.com/repos/nationalarchives/{repo}/tags"


def get_version(repository_name):
    print(f"Fetching tags for {repository_name}")
    tags = requests.get(url(repository_name), headers=headers).json()
    return tags[0]["name"]


def get_latest_versions():
    return dict((repository_name, get_version(repository_name)) for repository_name in tre_repositories)

