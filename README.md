# flask-todo

To do list using flask.

---

To set this project:

1. Environment

*virtualenvwrapper must be installed.

```bash
mkvirtualenv flask-todo 
...

git clone https://github.com/FredericoVieira/flask-todo.git
cd flask-todo
pip install -r requirements.txt --upgrade
```

* Set environment variables in ./virtualenvs/flask-todo/bin/activate

```bash
export DB_USER=root
export DB_PW=
export DB_HOST=localhost
export DB_RAW=flask_todo
```

2. Database

* MySQL must be installed.

Run create_database_flask_todo.sql and create_table_todo.sql

To run this project:

```bash
python run.py
```
