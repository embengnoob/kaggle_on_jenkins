import argparse
import sys
import subprocess
import logging as log
import random
import time

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--env', required=True, help="name of the conda environment to look for")
args = parser.parse_args()


def nmap():
    port = random.randint(8880, 8899)
    cmd = f'nmap -p{port} localhost'
    stdOut = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    return port, stdOut


def run_cmd(cmd):
    stdOut = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(stdOut)


def main():
    if not len(sys.argv) > 1:
        log.error("No argument was provided. Please provide a conda env name (-e <jenkins username>)")
        return 1
    user = args.env
    notebooksPath = 'F:\\jupyter_notebooks'
    # find a random free port for the local host
    (port, stdOut) = nmap()
    while 'open' in stdOut:
        (port, stdOut) = nmap()
    # start jupyter server
    log.warning('>>>>>>>>>>>>>>>>>>  Link to jupyter Notebook:   <<<<<<<<<<<<<<<<<<<<<')
    log.warning('>>>>>>>>>>>>>>>>>> http://134.109.204.54:%s <<<<<<<<<<<<<<<<<<<<<', str(port))
    cmd = f'jupyter lab --no-browser --ip 0.0.0.0 --port {port} --notebook-dir={notebooksPath}\\{user}'
    run_cmd(cmd)
    return 0


if __name__ == '__main__':
    sys.exit(main())