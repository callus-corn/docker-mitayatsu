import subprocess

subprocess.run(['docker', 'build', 'mysql', '-t', 'calluscorn/mysql:8.0'])
subprocess.run(['docker', 'push', 'calluscorn/mysql:8.0'])
