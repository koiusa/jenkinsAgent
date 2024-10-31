#!/usr/bin/env bash

pushd ./bin

./generate-serviceconfig.py
./download-agentjava.py

mkdir -p /opt/systemd/system
cp jenkins-agent.service /opt/systemd/system

popd

ln -sf /opt/systemd/system/jenkins-agent.service /etc/systemd/system/jenkins-agent.service
systemctl enable jenkins-agent
systemctl start jenkins-agent


