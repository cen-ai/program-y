#! /bin/sh
clear
export PYTHONPATH=../../src:../../libs/MetOffer-1.3.2:.
python3 ../../src/utils/test_runner/test_runner.py --test_dir ./aiml_tests/cen --verbose --config ./config.yaml --cformat yaml --logging ./logging.yaml --qna_file qna_file
