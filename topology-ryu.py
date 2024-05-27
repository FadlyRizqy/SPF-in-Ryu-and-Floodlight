#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork(num_switches):
    net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='10.0.2.15',
                           protocol='tcp',
                           port=6633)

    info('*** Add switches\n')
    switches = [net.addSwitch(f's{i}', cls=OVSKernelSwitch) for i in range(1, num_switches + 1)]

    info('*** Add hosts\n')
    hosts = [net.addHost(f'h{i}', cls=Host, ip=f'10.0.0.{i}', defaultRoute=None) for i in range(1, num_switches + 1)]

    info('*** Add links\n')
    for i in range(num_switches):
        net.addLink(hosts[i], switches[i])

    for i in range(num_switches):
        for j in range(i + 1, num_switches):
            net.addLink(switches[i], switches[j], cls=TCLink)

    info('*** Starting network\n')
    net.build()

    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    for switch in switches:
        switch.start([c0])

    info('*** Post configure switches and hosts\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')

    try:
        num_switches = int(input("Enter the number of switches: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit(1)

    myNetwork(num_switches)

