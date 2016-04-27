## About project

This is the example of ansible repository that shows how to organize managing your hosts with Ansible in one Git repository, how to use Ansible Galaxy and how to utilize [ansible-roles](https://github.com/andyceo/ansible-roles) repository with some common roles.


## System requirements

This version of playbooks and roles was tested only on:

  - Ubuntu 14.04
  - Ansible 1.5.4 (shipped with Ubuntu 14.04 with enabled backports)

Previous versions of Ansible and Ubuntu are not supported. If you interested in its support, please, provide patches.

Tip: You can install latest ansible from this [PPA](http://docs.ansible.com/ansible/intro_installation.html#latest-releases-via-apt-ubuntu):

    sudo apt-get install software-properties-common
    sudo apt-add-repository ppa:ansible/ansible
    sudo apt-get update
    sudo apt-get install ansible

Tip: Authentication with passphrase protected private-key require to enter passphrase for each server. You should execute following on the manager machine:

    ssh-agent bash
    ssh-add ~/.ssh/id_rsa

Then, execute playbooks.


## Usage

1. Install ansible on your manager machine:

        sudo aptitude install ansible

2. Clone this repository and change working directory to this repository (all following commands assumes that your working directory is this cloned repository directory):

        git clone git@github.com:andyceo/ansible-example.git
        cd ansible-example

3. If you cloned repository `ansible-example` without submodules, then execute following commands in root folder of `ansible-example` repository to install `ansible-roles` repository:

        git submodule init
        git submodule update

4. Install andyceo roles from Ansible Galaxy:

        ansible-galaxy install -r roles.txt --force

5. Add your target (remote) host name you want to operate with (for example, `example`) to inventory file: `ansible/hosts` or `ansible/hosts.py` (dynamic inventory)

6. Add file with your desirable config to `ansible/host_vars/example`. Use `ansible/host_vars/example` as example

7. Usage and runnig:

    - Ping hosts that match pattern `*ampl*` (host `example` will be pinged):

        ansible '*ampl*' -i hosts.py -m ping

    - Simulate `example.yml` playbook execution on host `example` and show posible differences that will be made by ansible:

        ansible-playbook -K -k -v -i hosts -l example example.yml --check --diff

    - Execute playbook `example.yml` on host `example` with verbose and dump information, asking passwords for ssh and sudo:

        ansible-playbook -K -k -v -i hosts -l example example.yml

    - Execute playbook with dynamic inventory:

        ansible-playbook -K -k -v -i hosts.py -l example example.yml
