#!/usr/bin/env python3
import subprocess
import signal
import shlex
import os

def killApplicationProcessIfStillRunning(app_name):
    p1 = subprocess.Popen(shlex.split('ps -ef'), stdout=subprocess.PIPE)
    p2 = subprocess.Popen(shlex.split(f'grep {app_name}', stdin=p1.stdout, stdout=subprocess.PIPE))
    p3 = subprocess.Popen(shlex.split('grep -v grep'), stdin=p2.stdout, stdout=subprocess.PIPE)
    p4 = subprocess.Popen(shlex.split("awk '{print $2}'", stdin=p3.stdout, stdout=subprocess.PIPE))
    out, err = p4.communicate()

    if out:
        print(f"Attemping to kill {app_name} process with PID {out.splitlines()[0]}")
        os.kill(int(out.splitlines()[0]), signal.SIGKILL)

def main():
    app_name = "yusstest.sh"
    killApplicationProcessIfStillRunning(app_name)

if __name__ == "__main__":
    main