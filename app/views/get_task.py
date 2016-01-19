from app import app
from flask import render_template, Blueprint

mod = Blueprint('get_task', __name__)

@mod.route('/')
def get_task():
    return render_template('get_task.html')