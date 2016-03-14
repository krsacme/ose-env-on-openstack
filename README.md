#OpenShift Enterprise Environment in OpenStack Platform

** work in progress **

Ansible based OpenShift Environment preparation on the OpenStack platform with following steps:
- Create the required VMs
- Setup the local DNS server via dnsmasq
- Dynamically adding new hosts to the same ansible run to configure the created nodes
- Create the hosts file required for the OpenShift installation
- Prepare the host environment with packages and configurations
- Create master1 as the installer and setup ssh with other nodes


####Usage:
Create the environement:
```
ansible-playbook vm_creation.yml
```

Destroy the environment:
```
ansible-playbook vm_deletion.yml
```
