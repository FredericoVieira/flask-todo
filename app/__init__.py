from flask import Flask

app = Flask(__name__)

from app.views.home import mod as home_module
from app.views.get_task import mod as get_task_module
from app.views.insert_task import mod as insert_task_module

app.register_blueprint(home_module)
app.register_blueprint(get_task_module)
app.register_blueprint(insert_task_module)