#OpenShift Enterprise Environment in OpenStack Platform

** work in progress **

Ansible based OpenShift Environment preparation on the OpenStack platform with following steps:
- Create the required VMs
- Setup the local DNS server via dnsmasq
- Create the hosts file required for the OpenShift installation
- Prepare the host environment with packages and configurations


####Usage:
Create the environement:
```
ansible-playbook vm_creation.yml
```

Destroy the environment:
```
ansible-playbook vm_deletion.yml
```
