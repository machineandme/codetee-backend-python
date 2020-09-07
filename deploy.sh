scp -r * root@64.227.116.164:shirts
ssh root@64.227.116.164 "bash -c 'cd shirts
killall python || true
sleep 1
killall screen || true
#pipenv install --skip-lock
screen -d -m pipenv run python server.py || true
sleep 1
wget -qO- 'http://localhost/' | head -1'"
