# salt-cloud-python-wrapper
A wrapper for salt-cloud for dynamically creating virtual machines on VMware with static IP

```
usage: provisioner.py [-h] [-n NAME] -a ADDRESS [-c CPUS] [-m MEM]
                      [-z {network1,network2}]

salt-cloud wrapper for deploying

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name of the VM
  -a ADDRESS, --address ADDRESS
                        IP address of VM
  -c CPUS, --cpu CPUS   the amount of cores
  -m MEM, --memory MEM  the amount of GB in RAM
  -z {network1,network2}, --zone {network1,network2}
                        the network zone of the VM
  ```

# dependecies
the script needs to be run from a salt-master with salt-cloud installed.
you should also install pyvmomi with pip if it hasn't been installed.

Tested on Centos 7.
