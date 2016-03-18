import os
from flask import Flask
from app.views.task import mod as task_module

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(task_module)

port = int(os.environ.get("PORT", 5000))