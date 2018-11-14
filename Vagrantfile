# -*- mode: ruby -*-
# vi: set ft=ruby :

# USAGE:
# We have two different Linux flavours. You may start the one you most
# are familiar with.
#
# vagrant up ubuntu
# vagrant up centos


Vagrant.configure(2) do |config|
  # SEE: https://github.com/hashicorp/vagrant/issues/9442
  #Vagrant::DEFAULT_SERVER_URL.replace('https://vagrantcloud.com')

  # NOTE: On Vagrant 1.8.5, there's a bug with Vagrant managing the default
  # private ssh key. More details: https://github.com/mitchellh/vagrant/issues/7610
  #
  # In this bug, Vagrant renews the default ssh private key to a newer one ONLY for you.
  # However, when Vagrant does it, it changes the .ssh/authorized_keys permissions and
  # set unix permission to 0644.
  #
  # This makes sshd_config thinks it's a security risk and denies connection coming from
  # the default vagrant user using 'vagrant ssh' command.

  # The fix was released on Vagrant 1.8.6 or newer. Depending on which version you are
  # using, you might need the following configuration below:

  if Vagrant::VERSION.to_s == '1.8.5'
    config.ssh.insert_key = false
  end

  config.vm.provider :virtualbox do |v|
    # Ubuntu is creating a kernel log file in the host machine called
    # ubuntu-xenial-16.04-cloudimg-console.log
    # This config below will prevent this.
    v.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
    v.memory = 512
    v.cpus = 2
  end

  config.vm.define :ubuntu, primary: false, autostart: false do |ubuntu|
    ubuntu.vm.box = "ubuntu/xenial64"
    ubuntu.vm.hostname = "ubuntu"
    ubuntu.vm.network "forwarded_port", guest: 8008, host: 9999

    ubuntu.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/ubuntu.yml"
      ansible.become = true
      ansible.become_user = "root"
      ansible.compatibility_mode = "2.0"
      # Ubuntu 18.04 LTS (Bionic Beaver) no longer has Python 2 installed.
      # Preparing for the future over here.
      ansible.extra_vars = { ansible_python_interpreter: "/usr/bin/python3" }
    end

  end


  config.vm.define :centos, primary: false, autostart: false do |centos|
    centos.vm.box = "centos/7"
    centos.vm.hostname = "centos"
    centos.vm.network "forwarded_port", guest: 8008, host: 8888

    centos.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/centos.yml"
      ansible.become = true
      ansible.become_user = "root"
      ansible.compatibility_mode = "2.0"
    end

    # This will be needed on Django settings.
    centos.vm.provision "shell", inline: "echo 'ENVIRONMENT=dev' > /etc/profile.d/tutorial_env.sh"

  end

end
