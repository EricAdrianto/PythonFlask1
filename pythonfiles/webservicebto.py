import subprocess
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        list_files = subprocess.run(["dir"])
        print(list_files)
    except:
        print("ERROR IN LIST FILES")
    return 'Hello, World!'

@app.route('/wsbto', methods=['POST'])
def create_task():
    if not request.json or not 'State' in request.json:
        abort(400)
    task = {
        'State': request.json['State'],
        'description': request.json.get('ProblemImpact', ""),
        'done': False
    }
    print(task)
    return jsonify({'task': task}),201