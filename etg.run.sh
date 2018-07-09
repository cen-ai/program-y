
echo apt-get install libxml2-dev libxslt-dev
echo pip3 install -r requirements.txt 
screen bots/cen/cen-flask-rest.production.etg.sh

echo curl 'http://localhost:8989/api/v1.0/ask?question=hello+world&sessionid=1234567890'


pm2 start /home/edguy/program-y/bots/cen/cen-flask-rest.production.etg.sh

or 
cd ~edguy/program-y/bots/cen/ ; pm2 start cen-flask-rest.production.etg.sh 


