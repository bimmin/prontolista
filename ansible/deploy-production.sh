#!/bin/bash

export GIT_COMMIT_SHORT=$(echo $CIRCLE_SHA1 | cut -c 1-8)
echo $VAULT_PASSWORD > vault-password-file
cp ../api/docker-compose.production.yml ./roles/deploy/files/
poetry run ansible-playbook -i production deploy.yml --extra-vars "tag=${GIT_COMMIT_SHORT} docker_compose_file=docker-compose.production.yml" --vault-password-file=vault-password-file
rm vault-password-file
