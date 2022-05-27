#!/bin/sh

# Install MongoDB
/etc/init.d/dbus start
mkdir -p /data/db
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 4B7C549A058F8B6B
echo "deb [arch=amd64] http://repo.mongodb.org/apt/ubuntu $(lsb_release -sc)/mongodb-org/4.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.2.list
apt update
yes "" | apt install -y --allow-unauthenticated mongodb-org

# Install Python 3.7
apt-get update
apt install -y build-essential checkinstall libreadline-gplv2-dev \
  libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev \
  libbz2-dev zlib1g-dev openssl libffi-dev python3-dev python3-setuptools wget

mkdir -pv /tmp/Python37/Python-3.7.10

(
  cd /tmp/Python37/ || exit 1

  wget https://www.python.org/ftp/python/3.7.10/Python-3.7.10.tar.xz
  tar xvf Python-3.7.10.tar.xz -C /tmp/Python37

  cd /tmp/Python37/Python-3.7.10/ || exit 1
  ./configure --enable-optimizations
  make altinstall
)

# Install dependencies
python3.7 -m pip install --upgrade pip
pip install -r requirements.txt
