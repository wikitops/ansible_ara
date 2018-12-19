import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    pkg = ["ara"]

    assert host.PipPackage(pkg).is_installed


def test_sources_directories(host):
    d = host.file("/etc/ara")
    assert d.exists
    assert d.is_directory
    assert d.user == 'root'
    assert d.group == 'root'


def test_config_file(host):
    f = host.file("/etc/ara/ara.cfg")

    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'


def test_service(host):
    s = host.service('ara')
    assert s.is_enabled
    assert s.is_running


def test_sockets_open(host):
    s = host.socket("tcp://127.0.0.1:9191")
    assert s.is_listening
