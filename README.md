JEE
===

[Ansible](https://docs.ansible.com/ansible/latest/index.html) role to provision a [Jakarta-EE](https://jakarta.ee) application server:

* [Wildfly](https://wildfly.org)

Supports Ubuntu and CentOS. Other distributions may work, too, if they run services with `systemd`.


Role Variables
--------------

| var                       | description | default |
| ------------------------- | ----------- | ------- |
| java_version              | What OpenJDK version to use | 11 |
| wildfly_version           | What version of WildFly to use | 18.0.0.Final |
| wildfly_archive_checksum  | The checksum of the WildFly archive | sha1:2d4778b14fda6257458a26943ea82988e3ae6a66 |
| wildfly_download_base_url | In case you need a different source for the WildFly archive | http://download.jboss.org/wildfly |

Example Playbook
----------------

    - hosts: workers
      roles:
         - { role: jee-ansible-role, java_version: 13 }

License
-------

Apache 2.0
