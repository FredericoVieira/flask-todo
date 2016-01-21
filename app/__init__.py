from flask import Flask

app = Flask(__name__)

from app.views.task import mod as task_module

app.register_blueprint(task_module)