#!/bin/bash
ansible-playbook ./deploy.yml --private-key=./ssh_keys/prod_key \
-u deployer -i ./hosts
