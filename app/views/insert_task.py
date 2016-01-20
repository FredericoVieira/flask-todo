from app import app
from flask import render_template, Blueprint, request
from werkzeug import secure_filename
from app.db import conn

mod = Blueprint('insert_task', __name__)

@mod.route('/insert_task', methods=['GET', 'POST'])
def insert_task():
	if request.method == "POST":
		form_data = request.form.to_dict()
		print form_data
		return "Success"
	return render_template('insert_task.html')
