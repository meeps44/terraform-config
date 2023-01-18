resource "digitalocean_droplet" "www-1" {
  count = 1

  image  = "ubuntu-20-04-x64"
  name   = "ubuntu-lon1-${count.index}"
  region = "lon1"
  size   = "s-2vcpu-2gb"
  ipv6   = true
  ssh_keys = [
    data.digitalocean_ssh_key.new-key.id
  ]

  connection {
    host        = self.ipv4_address
    user        = "root"
    type        = "ssh"
    private_key = file(var.pvt_key)
    timeout     = "2m"
  }

  provisioner "remote-exec" {
    inline = [
      "export PATH=$PATH:/usr/bin",
      "sudo apt update -y",
      "sudo apt upgrade -y",
      "apt install autoconf build-essential git libtool -y",
      "curl -L https://bootstrap.saltstack.com -o install_salt.sh",
      "sudo sh install_salt.sh -A 209.97.138.74"
    ]
  }
}
