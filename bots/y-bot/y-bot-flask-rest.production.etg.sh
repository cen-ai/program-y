#! /bin/sh

cd $(dirname $0)
pwd

#clear

touch /tmp/y-bot.log
PYTHONPATH=../../src:. python3 ../../src/programy/clients/flaskrest.py --config ./config.yaml --cformat yaml --logging ./logging.yaml 
#tail -f /tmp/y-bot.log



