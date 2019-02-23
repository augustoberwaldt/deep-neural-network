import argparse
import os

# Disable certificate warnings
import requests
requests.packages.urllib3.disable_warnings()

import xnat


def parse_arguments():
    parser = argparse.ArgumentParser(
            description='Download the CADDementia data to a target directory.',
            epilog='Note: this tool requires the xnatpy package which can be installed by: pip install xnat'
    )
    parser.add_argument('--directory', type=str, required=True, help='Directory to put results in (this will create a directory for the project inside the target directory)')
    parser.add_argument('--user', type=str, required=True, help='Username to use for logging in to XNAT')
    parser.add_argument('--project', type=str, default='caddemen-train', help='XNAT project to download')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    target_dir = args.directory
    user = args.user
    project = args.project

    # Make sure the output directory is created
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    elif os.path.isfile(target_dir):
        raise ValueError('Target directory is a file! Cannot overwrite!')

    with xnat.connect('https://xnat.bmia.nl/', user=user, verify=False) as connection:
        project = connection.projects[project]
        project.download_dir(target_dir) 


if __name__ == '__main__':
    main()
