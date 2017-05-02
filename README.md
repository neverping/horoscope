# Sample Django Application

This project is a small Django PoC, using Vagrant as local environment and Ansible as a configuration management.

This project was setup to be used under CentOS 7.3, but it would work on any other EL7 Linux distribution, such as Red Hat Enterprise Linux 7, Scientific Linux 7 or Oracle Linux. Ubuntu support still a WIP.

The project was is also using nginx as a webserver and gunicorn as a WSGI HTTP Server. MariaDB/MySQL as a database will be supported soon.

### TO HOW SETUP / INSTALL WITH VAGRANT

#### 1- Install VirtualBox

VirtualBox is a general-purpose full virtualizer for x86 hardware, and you can use it to host a virtual machine in your computer. It will be needed for this demo to host a Ubuntu or CentOS 7 machines.

1.1 - For MacOS and Windows users, you can download it from this URL below:

    https://www.virtualbox.org/wiki/Downloads

1.2 - For Ubuntu/Debian users, you can install it with the following command below:

    sudo apt-get install virtualbox

#### 2- Install Vagrant.

Vagrant is a command line utily for managing the lifecycle of virtual machines on a different types of providers. We will use VirtualBox as our provider.

2.1 - For MacOS and Windows users, you can download it from this URL below:

    https://www.vagrantup.com/downloads.html

2.2 - For Ubuntu/Debian users, you can install it with the following command below:

    sudo apt-get install vagrant

#### 3- Install Ansible.

Ansible is an open-source automation engine that automates software provisioning, configuration management, and application deployment.


3.1 - For MacOS, it is recommended using [Homebrew](https://brew.sh/) and installing it with the following command:

    brew install ansible

3.2 - For Ubuntu/Debian users, you can install it with the following command below:

    sudo apt-get install ansible

#### 4- Install Project requirements for local development using Virtualenv and pip.

It is recommended using Python Virtualenv for environment isolation between system packages and project packages.

You can check if you already have virtualenv by running (```virtualenv --version```) in your shell. Pip comes with virtualenv.

4.1 - For MacOS, you can download it from [here](https://pypi.python.org/pypi/virtualenv):

These are the steps for downloading and installing it.
```bash 
curl -so virtualenv.tgz https://pypi.python.org/packages/d4/0c/9840c08189e030873387a73b90ada981885010dd9aea134d6de30cd24cb8/virtualenv-15.1.0.tar.gz#md5=44e19f4134906fe2d75124427dc9b716 
tar zxf virtualenv.tgz 
cd virtualenv-15.1.0
python setup.py build 
sudo python setup.py install
``` 

4.2 - For Ubuntu/Debian users, you can install it with the following command below:<BR>

    sudo apt-get install python-virtualenv

After installing virtualenv, you may create your own Python environment and install the project requirements with the following steps:

```bash
virtualenv --unzip-setuptools ~/virtualenvs/sample_django_site
~/virtualenv/sample_django_site/bin/pip install -r requirements.txt
```

#### 5- Getting it up and running (finally!)

After all these steps completed, you can run this project using two methods:

5.1 - Running Django on your own machine:

```bash
cd tutorial
python manage.py migrate
python manage.py test
python manage.py runserver 0:9999
```

Open your favourite web browser and hit (```http://localhost:9999```)

5.2 - Running Django on the provisioned virtual machine.

```bash
vagrant up centos
```

After Vagrant finishes, you may open your favourite web browser and hit (```http://localhost:8888```)
