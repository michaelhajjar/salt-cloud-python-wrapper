#importing all the modules
from salt.cloud import CloudClient
import salt.client
import salt.config
import sys
import argparse


def create_vm(name, address, cpus, mem, net, gw):
    ''' create a VM on salt-cloud, dynamic profile '''
    client = salt.cloud.CloudClient(path='/etc/salt/cloud')
    client.create(
    provider='vmware', names=[name],
    template=False, clonefrom='template',
    num_cpus='1', cores_per_socket=cpus, memory=mem,

    devices={
    'network': {
      'Network adapter 1':
        {'name': net,
         'adapter_type': 'vmxnet3',
         'switch_type': 'distributed',
         'ip': address,
         'gateway': [gw],
         'subnet_mask': '255.255.255.0',
         'domain': 'domain.com'
         }
    }},
    
    domain='domain.com',
    ssh_username='root', password='password',
    cluster='cluster', datastore='datastore',
    folder='directory', datacenter='datacenter',
    power_on=True, deploy=True, dns_servers='dnsserver',
    wait_for_passwd_timeout='120', image='centos64Guest'
    )

def main(argv):
    # arguments for the cli
    parser = argparse.ArgumentParser(description="salt-cloud wrapper for deploying")
    
    parser.add_argument("-n", "--name", dest="name", action="store",
                        help="Name of the VM")

    parser.add_argument("-a", "--address", dest="address", required=True,
                        help="IP address of VM")

    parser.add_argument("-c", "--cpu", dest="cpus", default="1", action="store",
                        help="the amount of cores")
    
    parser.add_argument("-m", "--memory", dest="mem", action="store", default="2GB", 
                        help="the amount of GB in RAM")
  
    parser.add_argument("-z", "--zone", dest="zone", action="store", default="network1",
                        help="the network zone of the VM", choices=['network1', 'network2'])

    args = parser.parse_args()
    name = args.name 
    address = args.address
    cpus = args.cpus
    mem = args.mem
    zone = args.zone

				# define the networks you want the cli tool to have
    if zone == 'network1':
      nic = 'network1'
      gw4 = '192.168.2.0'
    elif zone == 'network2':
      nic = 'network2'
      gw4 = '192.168.1.0'
    
    create_vm(name, address, cpus, mem, nic, gw4)

if __name__ == "__main__":
    main(sys.argv)
