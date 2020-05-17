ssh root@64.227.116.164 "bash -c 'cd shirts
git pull
killall python
sleep 1
killall screen
#pipenv install --skip-lock
screen -d -m pipenv run python server.py
sleep 1
wget -qO- 'http://localhost/' | head -1'"
