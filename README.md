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


How to Use
----------

* Backup dump.rdb from /var/lib/redis and then `redis-cli flushall`

```
cd scripts
python populate_questions.py  # expects questions.json in the current folder
python generate_tokens.py <optional-number-of-tokens-to-generate>
python add_time.py <optional-time-in-minutes. Defaults to 20>

```
* At any point during the test, run `python calculate_scores.py` to generate the scores to stdout
