import os
import re
import testinfra.utils.ansible_runner
import yaml

testinfra_hosts = testinfra.utils.ansible_runner.\
    AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).\
    get_hosts('all')


# file dumped in `converge.yaml`
def read_ansible_vars(host):
    stream = host.file('/tmp/ansible-vars.yaml').content
    return yaml.safe_load(stream)


# get `var_name` from `ansible_vars`, resolving all `{{ var_name }}` blocks
def get_var(ansible_vars, var_name):
    value = ansible_vars[var_name]

    def replace(m):
        return str(ansible_vars[m.group(1)])
    value = re.sub(r'{{ ?([a-z_]+) ?}}', replace, value)
    return value


def test_java_is_installed(host):
    ansible_vars = read_ansible_vars(host)
    var_name = 'java_package_' + ansible_vars['ansible_pkg_mgr']
    package_name = get_var(ansible_vars, var_name)
    assert host.package(package_name).is_installed


def test_app_server_is_installed(host):
    ansible_vars = read_ansible_vars(host)
    start_script = get_var(ansible_vars, 'application_server_start_script')
    assert host.file(start_script).is_file


def test_app_server_is_listening(host):
    assert host.socket('tcp://0.0.0.0:8080').is_listening


# TODO reachable from the outside
# def test_app_server_is_reachable(host):
#     assert http localhost:8080 contains
#     '<h3>Your WildFly instance is running.</h3>'
