yes "" | apt install mongodb
service mongodb start
apt-get update
apt install -y build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev zlib1g-dev openssl libffi-dev python3-dev python3-setuptools wget
mkdir /tmp/Python37
mkdir /tmp/Python37/Python-3.7.10
cd /tmp/Python37/
wget https://www.python.org/ftp/python/3.7.10/Python-3.7.10.tar.xz
tar xvf Python-3.7.10.tar.xz -C /tmp/Python37
cd /tmp/Python37/Python-3.7.10/
./configure --enable-optimizations
make altinstall
cd /pdytr
python3.7 -m pip install --upgrade pip
pip install -r requirements.txt