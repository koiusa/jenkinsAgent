#!/usr/bin/env python

import configparser
import os
import pwd
import grp

conf = configparser.ConfigParser()
conf.read('../setting.ini', encoding='utf-8')

workdir = conf['AGENT']['workdir']
url = conf['SERVER']['url']

os.makedirs(f"{workdir}",exist_ok=True)

user = conf['ENV']['user']
uid = pwd.getpwnam(user).pw_uid
gid = grp.getgrnam(user).gr_gid
os.chown(workdir,uid,gid)

os.system(f"curl -o {workdir}/agent.jar {url}/jnlpJars/agent.jar")

