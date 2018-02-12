#!/usr/bin/env python3

from optparse import OptionParser
import configparser
import glob
import os


def build_tx_config(options):
    print('build config here..')

    config = configparser.ConfigParser()
    config['main'] = {'host': 'https://www.transifex.com'}

    if options.files:
        # if we sent files write a new config
        for file_name in options.files.split():
            print(file_name)
            add_to_config(options, config, file_name)
    else:
        # use what we have in the config in the repo
        pass

    with open('.tx/config', 'w') as configfile:
        config.write(configfile)


def add_to_config(options, config, file_name):
    if 'content/' in file_name or 'data/' in file_name:
        file_type = 'TXT'
        path, name = os.path.split(file_name)
        base, ext = os.path.splitext(name)
        resource = '{project}.{resource}'.format(project=options.project_slug, resource='')
        if file_name.endswith('.md'):
            file_type = 'GITHUBMARKDOWN'
        elif file_name.endswith('.json'):
            file_type = 'KEYVALUEJSON'
        elif file_name.endswith('.yaml'):
            file_type = 'YML'
        config[resource] = {}
        config[resource]['file_filter'] = 'content/{base}.<lang>.{ext}'.format(base=base, ext=ext)
        config[resource]['source_file'] = 'content/{name}'.format(name=name)
        config[resource]['source_lang'] = 'en_US'
        config[resource]['type'] = file_type


def main():
    parser = OptionParser(usage="usage: %prog [options] link_type")
    parser.add_option("-p", "--project_slug", help="tx project slug", default="")
    parser.add_option("-f", "--files", help="files to work with", default=None)
    (options, args) = parser.parse_args()

    build_tx_config(options)

if __name__ == "__main__":
    main()
