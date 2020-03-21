from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world(name=None):
    return render_template('objection_detection.html', name=name)
    #return 'Hello, World!'

@app.route('/local')
def hello_world2(name=None):
    return render_template('objection_detection_local.html', name=name)

@app.route('/localjay')
def hello_world3(name=None):
    return render_template('objection_detection_local_jayz.html', name=name)