import \
    os

import \
    testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.\
    AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).\
    get_hosts('all')

# TODO complete README


def test_java_is_installed(host):
    # TODO get package name from ansible vars
    # but that's not so easy: https://github.com/ansible/molecule/issues/151
    assert host.package('openjdk-11-jre-headless').is_installed


def test_wildfly_is_installed(host):
    assert host.file('/opt/wildfly/bin/standalone.sh').is_file


def test_wildfly_is_running(host):
    assert host.socket("tcp://0.0.0.0:8080").is_listening
