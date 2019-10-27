# twiggy

Util written in python to do "live" tweeting

## First time only

### Configuration

You need to take inspiration from `config_example.py` and create your own `config.py` file.

### Create a virtual environment

`virtualenv --python=/usr/bin/python3 venv`

## Always

### Activate the virtual environment

`source venv/bin/activate`

### Install dependencies

`pip install -r requirements.txt`

### Run script

`python twiggy.py --source tweets.txt --mode time|notime"`

## Useful in development

### Update requirements

`pip freeze > requirements.txt`
