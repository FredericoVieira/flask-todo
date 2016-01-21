import dataset

db = dataset.connect('sqlite:///tasks.db')
tasks = db['tasks']