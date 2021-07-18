#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

apt-get -y update
apt-get -y upgrade
apt-get -y install gunicorn gcc
apt-get -y install git
apt-get clean
rm -rf /var/lib/apt/lists/*
