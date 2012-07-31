README
======

MyCQ is a simple website written in Flask to give MCQ test

Installation
------------

* `sudo pip install -r requirements.txt`

Configuration
-------------

* `cp mycq/settings.py.sample mycq/settings.py`
* Edit mycq/settings.py
* `export PYTHONPATH=$PATH_TO_REPO_ROOT:$PYTHONPATH`
* `python populate_questions.py`
* `python generate_token.py <num of tokens>` to generate registration tokens
