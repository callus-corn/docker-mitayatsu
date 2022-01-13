import sys
import subprocess

if __name__ == '__main__':
    subprocess.run(['docker','build','-t','golang:1.17','golang'])
    subprocess.run(['docker','build','-t','mysql:8.0','mysql'])
