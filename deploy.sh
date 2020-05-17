ssh root@64.227.116.164 -c "cd shirts
git pull
killall python
sleep 1
pipenv install
pipenv run
python server.py &
disown
sleep 1
curl --request GET -sL --url 'http://localhost/'
"