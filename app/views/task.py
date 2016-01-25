from flask import Blueprint, render_template, request, jsonify
from werkzeug import secure_filename
from app.db import db, tasks
import json

mod = Blueprint('task', __name__)


@mod.route('/')
@mod.route('/home')
@mod.route('/home/')
def index():
    return render_template('task/index.html')

@mod.route('/create', methods=['POST','GET'])
def create():
    if request.method == "POST":
        form_data = request.form.to_dict()
        tasks.insert(form_data)
        return render_template('task/success_create.html')
    return render_template('task/create.html')

@mod.route('/delete', methods=['POST','GET'])
def delete():
    if request.method == "POST":
        taskId = request.form.get('id')
        tasks.delete(id=taskId)
        return render_template('task/success_delete.html', taskId=taskId)
    return render_template('task/delete.html')

@mod.route('/delete/<int:taskId>')
def delete_id(taskId):
        tasks.delete(id=taskId)

@mod.route('/edit/<int:taskId>')
def edit(taskId):
    return render_template('task/edit.html')

@mod.route('/show/<int:taskId>')
def show():
    task = tasks.find_one(id=taskId)
    return render_template('task/show.html', task=taskId)



# JSON
@mod.route('/get/<int:taskId>')
def get(taskId):
    pass

@mod.route('/all')
def all():
    result = db.query('SELECT id, taskName, taskDesc FROM tasks')
    allTasks = []
    for row in result:
        allTasks += [(row['id'], row['taskName'], row['taskDesc'])]

    return jsonify(task_list=allTasks)
    #return jsonify(task_list = [row for result in tasks.all()])
