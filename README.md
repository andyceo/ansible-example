ansible-example
=============


# About project #

This is the example ansible repository that shows how to utilize [ansible-roles](https://github.com/andyceo/ansible-roles) repository with common roles.


# System requirements #

This version of playbooks and roles was tested only on:

  - Ubuntu 13.10
  - Ansible 1.4.4+dfsg-1~ubuntu13.10.1 (installed from backports: `sudo aptitude install ansible/saucy-backports`)

Previous versions of Ansible and Ubuntu are not supported. If you interested in its support, please, provide patches.


# Usage #

1. Install ansible on your manager machine:

        sudo aptitude install ansible/saucy-backports

2. Add your target (remote) host to `km/ansible/hosts`

3. Add file with your desirable config to `km/ansible/host_vars/YOURTARGETHOSTNAME`. Use `km/ansible/host_vars/ubuntu1310` as example

4. If you cloned repository `ansible-example` without submodules, then execute following commands in root folder of `ansible-example` repository:

        git submodule init
        git submodule update

5. Run:

        ansible-playbook -K -k -v -i hosts -l <YOURTARGETHOSTNAME> install.yml
