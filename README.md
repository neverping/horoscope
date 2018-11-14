# Sample Django Application

This is a small Django PoC, using Vagrant as local environment and Ansible as a configuration management.

This project was setup to be used under CentOS 7.3, but it would work on any other EL7 Linux distribution, such as Red Hat Enterprise Linux 7, Scientific Linux 7 or Oracle Linux. There's also support for Ubuntu 16.04.

The project is also using nginx as a webserver and gunicorn as a WSGI HTTP Server. MariaDB/MySQL as a database will be supported soon.

### TO HOW SETUP / INSTALL WITH VAGRANT

#### 1- Install VirtualBox

VirtualBox is a general-purpose full virtualizer for x86 hardware, and you can use it to host a virtual machine in your computer. It will be needed for this demo to host a Ubuntu or CentOS 7 machines.

1.1 - For MacOS and Windows users, you can download it from this URL below:

    https://www.virtualbox.org/wiki/Downloads

1.2 - For Ubuntu/Debian users, you can install it with the following command below:

    $ sudo apt-get install virtualbox

#### 2- Install Vagrant

Vagrant is a command line utily for managing the lifecycle of virtual machines on a different types of providers. We will use VirtualBox as our provider.

2.1 - For MacOS and Windows users, you can download it from this URL below:

    https://www.vagrantup.com/downloads.html

2.2 - For Ubuntu/Debian users, you can install it with the following command below:

    $ sudo apt-get install vagrant

#### 3- Install Project requirements for local development using Virtualenv, Virtualenv-wrapper and pip.

When working with Python, it is strongly recommended using Virtualenv and Virtualenv Wrapper for environment isolation between Python system packages and Python project packages.

You can check if you already have virtualenv running ```virtualenv --version``` in your shell. Pip comes with virtualenv.

3.1 - For MacOS, you can download it from [here](https://pypi.python.org/pypi/virtualenv):

These are the steps for downloading and installing it.

```bash 
$ curl -so virtualenv.tgz https://files.pythonhosted.org/packages/d4/0c/9840c08189e030873387a73b90ada981885010dd9aea134d6de30cd24cb8/virtualenv-15.1.0.tar.gz
$ tar zxf virtualenv.tgz 
$ cd virtualenv-15.1.0
$ python setup.py build 
$ sudo python setup.py install
``` 

And now for Virtualenv Wrapper:

    $ sudo pip install virtualenvwrapper

<B>Note</B>: virtualenvwrapper keeps all the virtual environments in ~/.virtualenv while virtualenv keeps them in the project directory.

3.2 - For Ubuntu/Debian users, you can install it with the following command below:<BR>

    $ sudo apt-get install python-virtualenv virtualenvwrapper

After installing virtualenv and virtualenvwrapper, you need to close the Terminal and open it again, so your Bash profile will be updated and then you can start using virtualenv-wrapper. You can start working with virtualenv by doing the steps below for both Mac and Linux users.

```bash
$ mkvirtualenv sample_django_app
$ pip install -r requirements.txt
```

The output for both commands will be something like this:

```bash
Running virtualenv with interpreter /usr/bin/python2
New python executable in /home/$YOUR_USERNAME/.virtualenvs/sample_django_app/bin/python2
Also creating executable in /home/$YOUR_USERNAME/.virtualenvs/sample_django_app/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
(sample_django_app) $ <--- prompt will show your current virtualenv.

(...)

(sample_django_app) $ pip install -r requirements.txt 
Collecting Django==1.11.16 (from -r tutorial/requirements.txt (line 1))
(...)
Installing collected packages: pytz, Django, (...)
Successfully installed Django-1.11.16 (...)
```

#### 4- Getting it up and running (finally!)

After all these steps completed, you can run this project using two methods:

4.1 - Running Django on your own machine:

```bash
$ cd tutorial
$ python manage.py migrate
$ python manage.py test
$ python manage.py runserver 0:9999
```

Open your favourite web browser and hit ```http://localhost:9999```

4.2 - Running Django on the provisioned virtual machine.

4.2.1 - Running on CentOS machine:

    $ vagrant up centos

After Vagrant finishes, you may open your favourite web browser and hit ```http://localhost:8888```

4.2.2 - Running on Ubuntu machine:

    $ vagrant up ubuntu

After Vagrant finishes, you may open your favourite web browser and hit ```http://localhost:9999```
