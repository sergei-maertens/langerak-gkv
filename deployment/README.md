# Ansible

Ansible playbook(s) to deploy the application.

The host must be docker-enabled and correctly provisioned.

## Requirements

```bash
pip install ansible~=8.5.0
ansible-galaxy role install -r requirements.yml
ansible-galaxy collection install -r requirements.yml
```

Host:

* SSH access, as root user for Docker
* PostgreSQL database (standard install), 14 or higher
* Docker engine - the application is deployed as docker containers

## Usage

```bash
ansible-playbook -i environments/production/hosts deploy-app.yml
```
