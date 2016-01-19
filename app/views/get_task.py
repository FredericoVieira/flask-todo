from app import app
from flask import render_template, Blueprint
from app.db import conn

mod = Blueprint('get_task', __name__)

@mod.route('/get_task')
def get_task():
	engine = conn()
	print engine
	return render_template('get_task.html')