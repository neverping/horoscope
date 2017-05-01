# -*- mode: ruby -*-
# vi: set ft=ruby :

# USAGE:
# We have two different Linux flavours. You may start the one you most
# are familiar with.
#
# vagrant up ubuntu
# vagrant up centos


Vagrant.configure(2) do |config|
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
    v.memory = 512
    v.cpus = 2
  end

  config.vm.define :ubuntu, primary: false, autostart: false do |ubuntu|
    ubuntu.vm.box = "ubuntu/trusty64"
    #ubuntu.vm.network "forwarded_port", guest: 80, host: 8080
    ubuntu.vm.provision "shell" do |shell|

    shell.inline = <<-SCRIPT
      echo "PLACEHOLDER"
      SCRIPT
    end
  end


  config.vm.define :centos, primary: false, autostart: false do |centos|
    centos.vm.box = "centos/7"
    centos.vm.hostname = "centos"

    # setting the name on virtual_box GUI.
    #centos.vm.define "centos" do |centos|
    #end

    # Per provider hostname
    #centos.vm.provider :virtualbox do |vb|
    #    vb.name = "centos"
    #end

    centos.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/centos.yml"
      ansible.sudo = true
    end

    # This will be needed on Django settings.
    centos.vm.provision "shell", inline: "echo 'ENVIRONMENT=dev' > /etc/profile.d/tutorial_env.sh"


  end

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
  #   sudo apt-get install -y apache2
  # SHELL
end
