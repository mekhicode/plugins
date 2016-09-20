#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import requests
import time

hostnames = ["",]
username = ''
password = ''

def get_supervisor_rabbitmq_num():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Cookie": "auth=Z3Vlc3Q6Z3Vlc3Q%3D; m=34e2:|4e99:t|64b8:t",
        "Authorization": "Basic Z3Vlc3Q6Z3Vlc3Q=",
    }
    r = requests.get("http://0.0.0.0:15672/api/connections", headers=headers).json()
    count = len(r)
    if count < 30:
        for hostname in hostnames:
            paramiko.util.log_to_file('paramiko.log')
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname, username=username, password=password)
            transport = ssh.get_transport()
            session = transport.open_session()
            session.set_combine_stderr(True)
            session.get_pty()
            session.exec_command("sudo supervisorctl restart rabbit_consumer:*")
            stdin = session.makefile('wb', -1)
            stdout = session.makefile('rb', -1)
            stdin.write(password +'\n')
            stdin.flush()
            for line in stdout.read().splitlines():
                print 'host: %s: %s' % (hostname, line)

while True:
    get_supervisor_rabbitmq_num()
    time.sleep(1800)

