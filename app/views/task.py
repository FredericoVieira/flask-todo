from flask import Blueprint, render_template, request, jsonify
from werkzeug import secure_filename
from app.db import tasks
import json

mod = Blueprint('task', __name__)


@mod.route('/')
@mod.route('/home')
@mod.route('/home/')
def index():
    allTasks = tasks.all()
    return render_template('task/index.html', allTasks=allTasks)

@mod.route('/create', methods=['POST','GET'])
def create():
    if request.method == "POST":
        form_data = request.form.to_dict()
        tasks.insert(form_data)
        return render_template('task/success_create.html')
    return render_template('task/create.html')

@mod.route('/edit/<int:task_id>')
def edit(task_id):
    pass

@mod.route('/show/<int:task_id>')
def show():
    task = tasks.find_one(id=task_id)
    return render_template('task/show.html', task=task_id)

@mod.route('/delete/<int:task_id>')
def delete(task_id):
    pass


# JSON
@mod.route('/get/<int:task_id>')
def get(task_id):
    pass

@mod.route('/all')
def all():
    import pdb; pdb.set_trace()
    allTasks = tasks.all()
    json.dumps(allTasks, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    return jsonify(task_list=allTasks)
