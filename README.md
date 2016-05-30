#OpenShift Enterprise Environment in Cloud Platform (OpenStack & AWS)

** work in progress **

Ansible based OpenShift Environment preparation on the OpenStack platform with following steps:
- Create the required VMs in OpenStack Cloud (requires os_server module part of Ansbile 2.0)
- Setup the local DNS server via dnsmasq
- Dynamically adding new hosts to the same ansible run to configure the created nodes
- Create the hosts file required for the OpenShift installation
- Prepare the host environment with packages and configurations
- Create master1 as the installer and setup ssh with other nodes

Supported Images:
- Cloud Server Image
- Atomic Host Image

####Usage:

General configurable parameters are exposed at *group_vars/all* file.
The playbooks uses the named cloud parameter configured via [OpenStack Config](http://docs.openstack.org/developer/python-openstackclient/configuration.html). The parameter **named_cloud** is used to give the targetted OpenStack cloud configuration.


Create the environement:
```
ansible-playbook vm_creation.yml
```

Destroy the environment:
```
ansible-playbook vm_deletion.yml
```
