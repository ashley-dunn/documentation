#!/usr/bin/env python3

from optparse import OptionParser
import configparser
import glob


def build_tx_config(options):
    print('Would build config here..')
    print(options)
    # glob files

    config = configparser.ConfigParser()
    config['main'] = {'host': 'https://www.transifex.com'}

    #for f in glob.glob('*'):
    #add_to_config(glob.glob('*'))


def add_to_config(options, config, files):
    for f in files:
        file_type = 'TXT'
        resource = '{project}.{resource}'.format(project=options.project_slug, resource='')
        if options.branch_name:
            resource = '{branch}--{project}.{resource}'.format(branch=options.branch_name, project=options.project_slug, resource='')
        if f.endswith('.md'):
            file_type = 'GITHUBMARKDOWN'
        elif f.endswith('.json'):
            file_type = 'KEYVALUEJSON'
        elif f.endswith('.yaml'):
            file_type = 'YML'
        config[resource] = {}
        config[resource]['file_filter'] = 'content/_index.<lang>.md'
        config[resource]['source_file'] = 'content/_index.md'
        config[resource]['source_lang'] = 'en_US'
        config[resource]['type'] = file_type


def main():
    parser = OptionParser(usage="usage: %prog [options] link_type")
    parser.add_option("-p", "--project_slug", help="tx project slug", default="")
    parser.add_option("-b", "--branch_name", help="branch name to prepend", default="")
    (options, args) = parser.parse_args()

    build_tx_config(options)

if __name__ == "__main__":
    main()
