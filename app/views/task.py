from app import app
from flask import render_template, Blueprint, jsonify
from app.db import conn

mod = Blueprint('task', __name__ , url_prefix='/task')

@mod.route('/get/<id>')
def get():
    return render_template('get_task.html')


@mod.route('/list')
def list():
    task_list = [
            {'name': u'Task 1', 'description': u'description 1'},
            {'name': u'Task 2', 'description': u'description 2'},
            {'name': u'Task 3', 'description': u'description 3'},
        ]

    return jsonify(task_list=task_list)


@mod.route('/list_task')
def list_task():
    task_list = [
            {'name': u'Task 1', 'description': u'description 1'},
            {'name': u'Task 2', 'description': u'description 2'},
            {'name': u'Task 3', 'description': u'description 3'},
        ]

    return render_template('get_task.html', task_list=task_list)
