all: run

# the export is to run as module -> allow relative import
run:
	export FLASK_APP=app.main
	flask --app main.py run --debug

init:
	pip install -r requirements.txt