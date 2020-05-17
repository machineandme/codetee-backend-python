ssh root@64.227.116.164 "cd shirts
git pull
killall python
sleep 1
pipenv install --skip-lock
pipenv run python server.py &
disown
sleep 1
curl --request GET -sL --url 'http://localhost/'
exit 0"