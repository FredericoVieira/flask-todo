from app import app
from flask import render_template, Blueprint
from app.db import conn

mod = Blueprint('insert_task', __name__)

@mod.route('/insert_task')
def insert_task():
	engine = conn()
	print engine
	return render_template('insert_task.html')