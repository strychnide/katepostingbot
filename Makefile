setup:
	virtualenv .venv --python=pypy3
	. .venv/bin/activate; pip install -r requirements.txt -r requirements_dev.txt

start:
	. .venv/bin/activate; PORT=5000 python -m bot

lint:
	. .venv/bin/activate; python -m flake8 bot

clean:
	-rm -r .venv *.egg-info build dist docs/dist coverage .coverage

push:
	sudo heroku container:push web --recursive --app katepostingbot
	heroku container:release web --app katepostingbot
