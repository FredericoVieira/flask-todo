from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from werkzeug import secure_filename
from app.db import db, tasks
import json

mod = Blueprint('task', __name__)


@mod.route('/', methods=['GET'])
def index():
    return render_template('task/index.html')


@mod.route('/create', methods=['GET'])
def new():
    task = ''
    return render_template('task/create.html', task=task, action=url_for('task.create'))


@mod.route('/create', methods=['POST'])
def create():
    form_data = request.form.to_dict()
    tasks.insert(form_data)
    return redirect('/')


@mod.route('/show/<int:task_id>')
def show(task_id):
    task = tasks.find_one(id=task_id)
    return render_template('task/show.html', task=task)


@mod.route('/edit/<int:task_id>', methods=['GET'])
def edit(task_id):
    task = tasks.find_one(id=task_id)
    return render_template('task/edit.html', task=task, action=url_for('task.update', task_id=task_id))


@mod.route('/edit/<int:task_id>', methods=['POST'])
def update(task_id):
    form_data = request.form.to_dict()
    form_data['id']=task_id
    tasks.update(form_data, ['id'])
    return redirect('/')


@mod.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    tasks.delete(id=task_id)
    return redirect('/')


@mod.route('/contact/', methods=['GET'])
def contact():
    return render_template('task/contact.html')


@mod.route('/showall/', methods=['GET'])
def showall():
    tasks = db.query('SELECT id, name, description, status FROM tasks')
    return render_template('task/showall.html', tasks=tasks)


#JSON
@mod.route('/get/<int:task_id>')
def get(task_id):
    pass


@mod.route('/all')
def all():
    tasks = db.query('SELECT id, name, description, status FROM tasks')
    all_tasks = []
    for task in tasks:
        all_tasks += [(task['id'], task['name'], task['description'], task['status'])]

    return jsonify(task_list=all_tasks)
    #return jsonify(task_list = [task for tasks in tasks.all()])
