echo TimkaUserBot setup
pkg install fish
apt-get update && apt-get upgrade -y
apt-get install git -y
pkg install python
pkg install wget
apt install curl
pkg install openssh
echo Процесс установки завершён
echo TimkaUserBot
python main.py