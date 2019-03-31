#export FLASK_APP=./Server/HttpServer.py

setup:
	pip3 install -r requirements.txt

run:
	#python3 -m flask run
	python3 ./Server/HttpServer.py


test: setup
	nosetests -v -exe -w ./

test-coverage: test
	nosetests -vv --with-coverage --cover-package='domain,parsers,link_generator,task_launcher,server' -exe