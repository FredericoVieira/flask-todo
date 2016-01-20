from app import app
from flask import render_template, Blueprint

mod = Blueprint('home', __name__)

@mod.route('/')
@mod.route('/home/')
def home():
    return render_template('home.html')
