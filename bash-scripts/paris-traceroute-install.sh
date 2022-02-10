#!/usr/bin/env bash

mkdir -p ~/logs/$HOSTNAME
mkdir ~/git
cd ~/git
git clone https://github.com/meeps44/libparistraceroute.git
cd ~/git/libparistraceroute
mkdir m4
./autogen.sh
./configure
ldconfig
make
make install
export PATH=$PATH:~/git/libparistraceroute/paris-traceroute
ldconfig