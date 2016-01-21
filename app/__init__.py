from flask import Flask
from app.views.task import mod as task_module

app = Flask(__name__)

app.register_blueprint(task_module)