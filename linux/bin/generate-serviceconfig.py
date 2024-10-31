#!/usr/bin/env python

import configparser

source=r'''
[Unit]
Description=Jenkins Agent
After=network.target
Requires=network.target

[Service]
Type=simple
# optional file to provide environment variables (e.g. http_proxy, https_proxy):
#EnvironmentFile=/etc/sysconfig/jenkins
# TODO: adapt -jnlpUrl und -secret, as found on the web GUI: Jenkins > Nodes > ...
ExecStart=/usr/bin/java -jar ${WORKDIR}/agent.jar -url ${URL} -secret ${SECRET} -name ${NAME} -workDir "${WORKDIR}"
Restart=always
User=${USER}
RestartSec=20

[Install]
WantedBy=multi-user.target
'''

conf = configparser.ConfigParser()
conf.read('../setting.ini', encoding='utf-8')
source = source.replace("${URL}", conf['SERVER']['url'])
source = source.replace("${SECRET}", conf['AGENT']['secret'])
source = source.replace("${NAME}", conf['AGENT']['name'])
source = source.replace("${WORKDIR}", conf['AGENT']['workdir'])
source = source.replace("${USER}", conf['ENV']['user'])

outfile = 'jenkins-agent.service'
f = open(outfile, 'w')
f.write(source)

f.close()

print( source )
print(f'{outfile} generated!')

