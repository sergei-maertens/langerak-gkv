# Ansible

Ansible playbook(s) for deployment of the koningskerk.nu domain.

Contains the setup for OpenCart, phpBB3, MySQL, PostgreSQL, Apache,
nginx and Django.

## Requirements

```bash
pip install -r requirements.txt
```

You need ``root`` access to the server and access with the application user
``konkerk`` over SSH via public key.

## Usage

```bash
ansible-playbook -i environments/production/hosts full-deploy.yml
```
