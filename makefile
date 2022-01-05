start:
	export FLASK_APP=server.py
	flask run

lint:
	flake8

fixlint:
	autopep8 --in-place --recursive .

.PHONY: start lint fixlint