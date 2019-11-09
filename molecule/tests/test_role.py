import os
import testinfra.utils.ansible_runner
import yaml

testinfra_hosts = testinfra.utils.ansible_runner.\
    AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).\
    get_hosts('all')

# TODO complete README


def read_ansible_vars(host):
    stream = host.file('/tmp/ansible-vars.yaml').content
    return yaml.safe_load(stream)


def test_java_is_installed(host):
    ansible_vars = read_ansible_vars(host)
    # resolution of derived variables doesn't work out-of-the-box,
    # so we couldn't use 'java_package'
    java_version = ansible_vars['java_version']
    package_name = 'openjdk-{}-jre-headless'.format(java_version)
    assert host.package(package_name).is_installed


def test_wildfly_is_installed(host):
    assert host.file('/opt/wildfly/bin/standalone.sh').is_file


def test_wildfly_is_running(host):
    assert host.socket("tcp://0.0.0.0:8080").is_listening


# TODO reachable from the outside
# def test_wildfly_is_reachable(host):
#     assert http localhost:8080
