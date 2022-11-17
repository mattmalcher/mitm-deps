# -*- mode: ruby -*-
# # vi: set ft=ruby :


nodes = [
  { :hostname => 'mitm-server', :ram => '2048', :cpus => '2' }, 
  { :hostname => 'mitm-client', :ram => '4096', :cpus => '4' }
]

Vagrant.configure("2") do |config|

    # Provision swarm nodes
    nodes.each do |node|
        config.vm.define node[:hostname] do |nodeconfig|
            nodeconfig.vm.box = "debian/bullseye64"
            
            nodeconfig.vm.hostname = node[:hostname] #+ ".box"

            # Network config depending on if server or client
            if node[:hostname] == 'mitm-server'
                nodeconfig.vm.network "private_network", ip: "10.0.3.3", netmask: "255.255.255.0", virtualbox__intnet: "mitmdeps"
                # disable rsync plugin
                nodeconfig.vm.synced_folder '.', '/vagrant', :disabled => true
            end

            if node[:hostname] == 'mitm-client'
                nodeconfig.vm.network "private_network", ip: "10.0.3.4", virtualbox__intnet: "mitmdeps"
                
                # Add NFS private network & enable sharing the deps folder to the guest
                nodeconfig.vm.network "private_network", type: "dhcp",  name: "vboxnet0"               
               
            end
            
            nodeconfig.ssh.insert_key = FALSE
            
            # set resources based on list
            nodeconfig.vm.provider "virtualbox" do |vb|
                vb.memory = node[:ram]
                vb.cpus = node[:cpus]
            end

            # provision both once you get to the second machine
            if node[:hostname] == 'mitm-client'
                nodeconfig.vm.provision "ansible" do |ansible|   
                    # Disable default limit to connect to all the machines        
                    ansible.limit = "all" 
                    ansible.playbook = "provisioning/bootstrap.yml"  
                end
            end

            # provision both once you get to the second machine
            if node[:hostname] == 'mitm-client'
                nodeconfig.vm.provision "ansible", run: "always" do |ansible|   
                    # Disable default limit to connect to all the machines        
                    ansible.limit = "all" 
                    ansible.playbook = "provisioning/route.yml"  
                end
            end

            # hardware setup            
            nodeconfig.vm.provider :virtualbox do |vb|
                # Enable virtual USB controller
                vb.customize ["modifyvm", :id, "--usb", "on", "--usbehci", "on"]
            end

            # server allows promiscuous mode on internal network
            if node[:hostname] == 'mitm-server'
                nodeconfig.vm.provider :virtualbox do |vb|
                    vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
                end
            end

            # provision both once you get to the second machine
            if node[:hostname] == 'mitm-client'
                nodeconfig.vm.provision "ansible", run: "always" do |ansible|   
                    # Disable default limit to connect to all the machines        
                    ansible.limit = "all" 
                    ansible.playbook = "provisioning/nfs.yml"  
                end
            end                        
        end
    end
end
