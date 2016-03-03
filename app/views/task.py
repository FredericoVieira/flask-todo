from flask import Blueprint, render_template, redirect, url_for, request, jsonify
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
        return redirect('/home')
    return render_template('task/create.html', action=url_for('task.create'))


@mod.route('/delete/<int:task_id>', methods=['POST','GET'])
def delete(task_id):
    if request.method == "POST":
        tasks.delete(id=task_id)
    return redirect('/home')


@mod.route('/edit/<int:task_id>', methods=['POST','GET'])
def edit(task_id):
    if request.method == "GET":
        task = tasks.find_one(id=task_id)
        return render_template('task/edit.html', task=task, action=url_for('task.edit', task_id=task_id) )

    elif request.method == "POST":
        form_data = request.form.to_dict()
        form_data['id']=task_id
        tasks.update(form_data, ['id'])
        return redirect('/home')


@mod.route('/show/<int:task_id>')
def show(task_id):
    task = tasks.find_one(id=task_id)
    return render_template('task/show.html', task=task)


#JSON
@mod.route('/get/<int:task_id>')
def get(task_id):
    pass


@mod.route('/all')
def all():
    result = db.query('SELECT id, taskName, taskDesc FROM tasks')
    allTasks = []
    for row in result:
        allTasks += [(row['id'], row['taskName'], row['taskDesc'])]

    return jsonify(task_list=allTasks)
    #return jsonify(task_list = [row for result in tasks.all()])
