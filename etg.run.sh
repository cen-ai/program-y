
echo apt-get install libxml2-dev libxslt-dev
echo pip3 install -r requirements.txt 
screen bots/y-bot/y-bot-flask-rest.production.etg.sh

echo curl 'http://localhost:8989/api/v1.0/ask?question=hello+world&sessionid=1234567890'
