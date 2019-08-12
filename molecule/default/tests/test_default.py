import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_executable(host):
    assert host.file('/usr/bin/docker').exists


def test_unix_socket(host):
    assert host.socket("unix:///var/run/docker.sock").is_listening


def test_group_membership(host):
    assert "docker" in host.user("test").groups
