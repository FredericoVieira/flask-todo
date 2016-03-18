#!flask/bin/python
from app import app, port

app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)