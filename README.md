[![Build Status](https://travis-ci.org/bihealth/ansible-role-docker.svg?branch=master)](https://travis-ci.org/bihealth/ansible-role-docker)

# Docker Community Edition

Basic setup of Docker Community Edition.

## Requirements

none

## Role Variables

See `defaults/main.yml` for all role variables and their documentation.

## Dependencies

none

## Example Playbook


```yaml
- hosts: servers
  roles:
    - role: bihealth.docker_ce
```

## License

MIT

## Author Information

- Manuel Holtgrewe

Created with love at [Core Unit Bioinformatics (CUBI), Berlin Institute of Health (BIH)](https://www.cubi.bihealth.org).
