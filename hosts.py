#!/usr/bin/env python

import __future__
import json, sys, getopt, socket

inventory = {
    'workstations': {
        'hosts': [
            'ubuntu1310'
        ]
    }
}

# Add current local hostname to the hosts list
inventory['workstations']['hosts'].append(socket.gethostname())

def get_hosts_list():
    hosts = set()
    for k, v in inventory.items():
        if 'hosts' in v:
          hosts.update(v['hosts'])
    return list(hosts)

def get_host_vars(host):
    hostname = socket.gethostname()
    host_vars = {}
    if host == hostname:
        host_vars['ansible_connection'] = 'local'
    return host_vars

def print_help():
    print('Usage:')
    print('    hosts.py --help')
    print('    hosts.py --hosts')
    print('    hosts.py --list [same as --hosts]')
    print('    hosts.py --host <hostname>')


########################################################

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h",["help", "hosts", "list", "host="])
    except getopt.GetoptError:
        print('Options error!')
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_help()
            sys.exit()
        elif opt == '--hosts':
            print(json.dumps(get_hosts_list(), indent=4, sort_keys=True))
            sys.exit()
        elif opt == '--host':
            print(json.dumps(get_host_vars(arg), indent=4, sort_keys=True))
            sys.exit()

    print(json.dumps(inventory, indent=4, sort_keys=True))
