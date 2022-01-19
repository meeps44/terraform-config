resource "digitalocean_droplet" "www-1" {
    count = 1
    
    image = "ubuntu-20-04-x64"
    name = "ubuntu-${count.index}"
    region = "lon1"
    size = "s-1vcpu-1gb"
    ipv6 = true
    ssh_keys = [
      data.digitalocean_ssh_key.new-key.id
    ]

connection {
    host = self.ipv4_address
    user = "root"
    type = "ssh"
    private_key = file(var.pvt_key)
    timeout = "2m"
  }

provisioner "remote-exec" {
    inline = [
      "export PATH=$PATH:/usr/bin",
      "sudo apt update",
      "apt install autoconf build-essential git libtool",
      "curl -L https://bootstrap.saltstack.com -o install_salt.sh",
      "sudo sh install_salt.sh -A 209.97.138.74",
      "mkdir ~/git",
      "cd ~/git",
      "git clone https://github.com/meeps44/libparistraceroute.git",
      "cd ~/git/libparistraceroute",
      "mkdir m4",
      "./autogen.sh",
      "./configure",
      "ldconfig",
      "make",
      "make install",
      "export PATH=$PATH:~/git/libparistraceroute/paris-traceroute"
    ]
  }
}
