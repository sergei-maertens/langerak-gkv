# Ansible

Ansible playbook(s) for deployment of the koningskerk.nu domain.

Contains the setup for PostgreSQL, nginx and Django.

## Requirements

```bash
pip install ansible==2.4.6.0
```

You need ``root`` access to the server and access with the application user
``konkerk`` over SSH via public key.

## Usage

```bash
ansible-playbook -i environments/production/hosts full-deploy.yml
```
