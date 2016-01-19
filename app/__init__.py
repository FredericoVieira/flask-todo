from flask import Flask

app = Flask("flask-todo")
app.config.from_object('config')

from app.general.views import mod as home_module
from app.insertdata.views import mod as get_task_module
from app.showdata.views import mod as insert_task_module

app.register_blueprint(home_module)
app.register_blueprint(get_task_module)
app.register_blueprint(insert_task_module)