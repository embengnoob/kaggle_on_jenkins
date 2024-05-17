import hashlib
import sys
import os
import json
import logging as log
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--env', required=True, help="name of the conda environment to look for")
args = parser.parse_args()

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    if not len(sys.argv) > 1:
        log.error("No argument was provided. Please provide a conda env name (-e <jenkins username>)")
        return 1
    user = args.env
    md5_path = f'F:\jenkins_scripts\md5_{user}.json'
    env_path = f'F:\jenkins_scripts\environment_{user}.yml'

    log.warning(' Jenkins conda environment updated. Rewriting md5 checksum ...')
    os.remove(md5_path)
    data = {'checksum': md5(env_path)}
    with open(md5_path, 'w') as f:
        json.dump(data, f)
    return 0 

if __name__ == '__main__':
    sys.exit(main())