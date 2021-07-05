#!/bin/sh

apt update

apt install -y ansible

cd /home/shared/

ansible-playbook -i targets install-playbook.yml

# cd ./docker-elk/

# docker-compose up --build -d

# cd ../mongodb

# docker-compose up -d


