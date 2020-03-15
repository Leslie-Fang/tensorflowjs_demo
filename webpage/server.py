from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world(name=None):
    return render_template('classification_load_json_model.html', name=name)
    #return 'Hello, World!'