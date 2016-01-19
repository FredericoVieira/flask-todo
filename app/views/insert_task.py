from app import app
from flask import render_template, Blueprint

mod = Blueprint('insert_task', __name__)

@mod.route('/')
def insert_task():
    return render_template('insert_task.html')