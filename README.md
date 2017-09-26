# Logs-Analysis
=============
## Setting up
### 1.Install Vagrant (link: https://www.vagrantup.com/downloads.html) and Virtualbox (link: https://www.virtualbox.org/wiki/Downloads)
### 2.Download the VM Configuration folder "fsnd-virtual-machine" (link: https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).
### 3.Download the SQL data "newsdata.sql" (link: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip it, and then put it inside folder "vagrant"
### 4.Right click on folder "vagrant", click on "Git Bash here", a git bash terminal is open.
### 5.On the git bash terminal, set up vagrant by first running command `vagrant up`, second `vagrant ssh`. A "Ubuntu 16.04.3 LTS" virtual machine is built up.
### 6.Run command `cd /vagrant`, ans then `ls`.
### 7.Run command `psql -d news -f newsdata.sql` to load the SQL data "newsdata.sql".
### 8.After loading "newsdata.sql", run `psql news` to explore the data.
